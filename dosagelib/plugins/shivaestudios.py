# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2021 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from .common import _WordPressSpliced


class _WithSid(_WordPressSpliced):
    def __init__(self, name, sid, eol=False):
        super().__init__(name)
        self.stripUrl = self.baseUrl + 'comic/%s/?sid={}'.format(sid)


class AbbysAgency(_WordPressSpliced):
    url = 'https://abbysagency.us/'
    stripUrl = url + 'blog/comic/%s/'
    firstStripUrl = stripUrl % 'a'


class AlienDice(_WordPressSpliced):
    url = 'https://aliendice.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '05162001'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filename
        return imageUrl.rsplit('/', 1)[-1].replace('20010831', '2001-08-31')


class AlienDiceLegacy(_WordPressSpliced):
    name = 'AlienDice/Legacy'
    url = 'https://aliendice.com/chapter/legacy/'
    stripUrl = url + 'page/%s/'
    firstStripUrl = stripUrl % '45'
    prevSearch = '//div[d:class("nav-previous")]/a'
    endOfLife = True


class BlackRose(_WordPressSpliced):
    url = 'https://www.blackrose.monster/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '2004-11-01'


class TheCyantianChronicles(_WithSid):
    baseUrl = 'https://cyantian.net/'

    def __init__(self, name, path, first, sid, eol=False):
        super().__init__('TheCyantianChronicles/' + name, sid)
        self.url = self.baseUrl + 'series/' + path + '/'
        self.firstStripUrl = self.stripUrl % first
        self.endOfLife = eol

    @classmethod
    def getmodules(cls):
        return (
            cls('Akaelae', 'akaelae', '05182003', 15043, eol=True),
            cls('Artwork', 'art-gallery', '07162003', 15102),
            cls('CampusSafari', 'original-campus-safari', '10012000', 13804, eol=True),
            cls('CampusSafariReboot', 'campus-safari', 'campus-safari-chapter-0', 13790),
            cls('CesileesDiary', 'cesilees-diary', '12062001-2', 16726, eol=True),
            cls('Darius', 'darius', '03102010', 14353, eol=True),
            cls('DracoVulpes', 'draco-vulpes', 'draco-vulpes', 13788),
            cls('GenoworksSaga', 'genoworks-saga', '07012004', 13794, eol=True),
            cls('GralenCraggHall', 'kiet', '07152002', 13798, eol=True),
            cls('Kiet', 'kiet-2', 'kiet-c01', 14351, eol=True),
            cls('NoAngel', 'no-angel', '08112001', 16644, eol=True),
            cls('RandomRamblings', 'gallery', 'cookie-war', 13801),
            cls('SinkOrSwim', 'sink-or-swim', '05112001', 13796, eol=True),
            cls('VincentAndFilaire', 'vincent-and-filaire', 'vincent-and-filaire', 13792),
        )


class Shivae(_WordPressSpliced):
    url = 'https://shivae.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '09202001'


class ShivaeComics(_WithSid):
    baseUrl = 'https://shivae.net/index.php/'

    def __init__(self, name, path, first, sid, eol=False):
        super().__init__('Shivae/' + name, sid)
        self.url = self.baseUrl + 'series/' + path + '/'
        self.firstStripUrl = self.stripUrl % first
        self.endOfLife = eol

    @classmethod
    def getmodules(cls):
        return (
            cls('Pure', 'pure-2', '2002-02-27', 1328, eol=True),
            cls('SerinFairyHunter', 'pure', 'character-serin', 1289),
            cls('SivineBlades', 'sivine-blades', '2002-06-30', 1326, eol=True),
        )
