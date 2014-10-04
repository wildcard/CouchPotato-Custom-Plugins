import re
import traceback

from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.rss import RSS
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
from urlparse import urlparse, parse_qs

log = CPLog(__name__)


class DownRev(MovieProvider, TorrentProvider, RSS):

    urls = {
        'test' : 'https://www.downrev.net/',
        'login' : 'https://www.downrev.net/takelogin.php',
        'detail' : 'https://www.downrev.net/torrent/%s',
        'search' : 'https://www.downrev.net/rss2.php?cats=%d&type=dl&passkey=%s&like=%s',
        'download' : 'https://www.downrev.net/down.php?id=%s&passkey=%s',
        'login_check': 'http://www.downrev.net/inbox',
    }

    cat_ids = [
        ([68], ['1080p']),
        ([45], ['720p']),
        ([36], ['dvdrip', 'scr', 'r5']),
        ([65], ['brrip']),
        ([34], ['dvdr']),
    ]

    http_time_between_calls = 1 #seconds

    def _searchOnTitle(self, title, media, quality, results):

        # strip special chars for search
        pattern = re.compile(r'[^a-zA-Z0-9\s]')
        _movieTitle = pattern.sub('', title)
        # replace ' ' by '.'
        _movieTitle = _movieTitle.replace(' ', '.')

        url = self.urls['search'] % (self.getCatId(quality)[0], self.conf('passkey'), _movieTitle)
        data = self.getRSSData(url, opener = self.login_opener)

        if data:
            try:
                for result in data:
                    title = self.getTextElement(result, "title")
                    desc = self.getTextElement(result, "description")
                    link = self.getTextElement(result, "link")

                    # Extract from link
                    o = urlparse(link)
                    ID = parse_qs(o.query)['id'][0]

                    p = re.compile(r'\W*Size[^: ]*:\s*(\d+.\d+\s\w+)\D*Leechers[^: ]*:\s(\d+)\D*Seeders[^: ]*:\s(\d+)')
                    m2 = p.findall(desc.replace('/', '').replace('<br/>', ''))

                    size = m2[0][0]
                    leechers = m2[0][1]
                    seeders = m2[0][2]

                    results.append({
                        'id': ID,
                        'name': title,
                        'url': self.urls['download'] % (ID, self.conf('passkey')),
                        'detail_url': self.urls['detail'] % ID,
                        'size': self.parseSize(size),
                        'seeders': tryInt(seeders),
                        'leechers': tryInt(leechers)
                    })

            except:
                log.error('Failed getting results from %s: %s', (self.getName(), traceback.format_exc()))

