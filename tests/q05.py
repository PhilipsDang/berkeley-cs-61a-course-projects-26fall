from pytest_grader import points


@points(0)
def autocorrect():
    r"""
    >>> from cats import autocorrect, lines_from_file
    >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
    >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
    LOCKED: 9d0b55ac067fc4fb
    >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
    LOCKED: 542aefd69a5434f5
    >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
    LOCKED: 31b1cf9a61b740f0
    >>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
    >>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
    LOCKED: b492b09ae1eca6e6
    >>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
    LOCKED: 0a0eeab180abe920
    >>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
    LOCKED: 2b426003f289727f
    >>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
    LOCKED: 97dd5dfff2098104
    """


@points(2)
def autocorrect_examples():
    r"""
    >>> from cats import autocorrect, lines_from_file
    >>> length_ratio = lambda w1, w2, limit: len(w2) / len(w1) # An asymmetric diff function
    >>> autocorrect("aaa", ["a"], length_ratio, 2) # typed_word ("aaa") is passed in as the first argument to a diff function
    'a'
    >>> autocorrect("cats", ["panthers", "lions"], length_ratio, 2)
    'lions'
    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    >>> matching_diff = lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) # Num matching chars
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], matching_diff, 10)
    'testing'
    >>> autocorrect("tsting", ["testing", "rowing"], matching_diff, 10)
    'rowing'
    >>> autocorrect("bwe", ["awe", "bye"], matching_diff, 10)
    'awe'
    >>> autocorrect("bwe", ["bye", "awe"], matching_diff, 10)
    'bye'
    >>> words_list = sorted(lines_from_file('data/words.txt')[:10000])
    >>> autocorrect("testng", words_list, lambda w1, w2, limit: 1, 10)
    'a'
    >>> autocorrect("testing", words_list, lambda w1, w2, limit: 1, 10)
    'testing'
    >>> autocorrect("gesting", words_list, lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) + abs(len(w1) - len(w2)), 10)
    'getting'
    >>> autocorrect('stilter', ['modernizer', 'posticum', 'undiscernible', 'heterotrophic', 'waller', 'marque', 'dephosphorization'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
    'posticum'
    >>> autocorrect('bridgemaking', ['seeds', 'bridgemaking', 'endemiological', 'cobaltinitrite'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'bridgemaking'
    >>> autocorrect('excursively', ['cirsotomy', 'terminableness', 'margaritaceous', 'gawkiness', 'ascon', 'floccose'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
    'excursively'
    >>> autocorrect('hypertense', ['hyperbrachycranial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'hypertense'
    >>> autocorrect('sporidia', ['intrarachidian', 'solifidianism'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'sporidia'
    >>> autocorrect('chanson', ['upanishadic', 'ftp', 'chanson', 'unbeached', 'astrolabical'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'chanson'
    >>> autocorrect('turnrow', ['lokao', 'archipelagian'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'turnrow'
    >>> autocorrect('fc', ['anthracia'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
    'fc'
    >>> autocorrect('crapy', ['nihilification', 'krieker', 'laureate', 'antechamber', 'crapy', 'belkin', 'ixodian', 'scarletseed', 'reliner', 'ebullioscope'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'crapy'
    >>> autocorrect('auximone', ['auximone'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
    'auximone'
    >>> autocorrect('semicheviot', ['cinematize', 'struma'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'semicheviot'
    >>> autocorrect('modify', ['imminution', 'uncensuring', 'fungiform', 'cargoose', 'quizzish'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'cargoose'
    >>> autocorrect('testator', ['impercipient', 'overrude', 'hyperingenuity', 'piligerous', 'molybdocolic', 'toxicum'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'overrude'
    >>> autocorrect('unabsorb', ['unabsorb', 'chromolithographic', 'hemadynamometer', 'frailly', 'diana'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'unabsorb'
    >>> autocorrect('bounteously', ['universalization', 'accroach', 'unflinchingly', 'seagoer', 'overlight', 'condoling', 'truckling'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'unflinchingly'
    >>> autocorrect('accomplisher', ['purloin', 'assignable', 'unallayably', 'caeca'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
    'unallayably'
    >>> autocorrect('zonal', ['cautery', 'wiseness', 'yobi', 'kirk', 'herbalism', 'separata', 'zonal', 'anaglyphic', 'unshrined'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'zonal'
    >>> autocorrect('associated', ['cardiodysneuria', 'provoker'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'provoker'
    >>> autocorrect('scusation', ['tubuliporoid', 'malleability', 'scusation', 'semichivalrous', 'urocele', 'dietetic', 'featureful', 'splenatrophy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'scusation'
    >>> autocorrect('proportionability', ['psychonomic', 'nonfuturity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'proportionability'
    >>> autocorrect('untenanted', ['musterable', 'multivincular', 'recuperator', 'goto', 'turnsole', 'untenanted', 'isopterous', 'carbanilic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
    'untenanted'
    >>> autocorrect('widespread', ['bogland', 'interclash'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'interclash'
    >>> autocorrect('arenilitic', ['maximization'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'maximization'
    >>> autocorrect('insee', ['karyopyknosis', 'nightwork', 'short', 'insee', 'unmated', 'capacitation'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'insee'
    >>> autocorrect('monoxenous', ['thoraces', 'preworldliness', 'monoxenous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'monoxenous'
    >>> autocorrect('outskirmisher', ['slatternly', 'hexadic', 'immaculateness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'outskirmisher'
    >>> autocorrect('unrepugnant', ['cordiner'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
    'unrepugnant'
    >>> autocorrect('arisen', ['palaeoatavism', 'drowsiness', 'untopped'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'untopped'
    >>> autocorrect('seafare', ['seafare', 'bimillennium', 'valviform', 'thyridial', 'umbones', 'logitech', 'indigestible', 'unfastidious', 'gammerel', 'valiseful'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'seafare'
    >>> autocorrect('uncranked', ['mesodermic', 'fingerling', 'metallophone'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'mesodermic'
    >>> autocorrect('unmagic', ['effluviate', 'unhuman', 'energeia', 'slouch', 'resource'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'unhuman'
    >>> autocorrect('tablespoon', ['tablespoon'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'tablespoon'
    >>> autocorrect('interwrought', ['rutabaga', 'fomentation', 'swampside', 'unpopularness', 'magnifier'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'fomentation'
    >>> autocorrect('plumosity', ['introspectionist', 'teeting', 'unbroiled'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'unbroiled'
    >>> autocorrect('staurolatry', ['staurolatry'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
    'staurolatry'
    >>> autocorrect('nonviscous', ['previdence'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'previdence'
    >>> autocorrect('sterile', ['emancipation', 'recedent', 'haustement', 'prorebate', 'weatherliness', 'unchristianity', 'nonprotection', 'deviousness', 'strangury', 'mauvine'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'mauvine'
    >>> autocorrect('propylic', ['touch', 'uniparental', 'chomp', 'violety', 'overweave', 'phelloplastics', 'fipple', 'inappreciable', 'melodramatist', 'pawnbrokering'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'propylic'
    >>> autocorrect('beechy', ['breastrope', 'hypocist', 'supersemination', 'ethnographically', 'atwitch', 'wraxle'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'wraxle'
    >>> autocorrect('stream', ['lecideiform', 'debtless', 'stream', 'loquent', 'leery', 'antipodean', 'mesothesis', 'ay'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
    'stream'
    >>> autocorrect('chevronelly', ['nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations', 'figent', 'mentality'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
    'chevronelly'
    >>> autocorrect('windbracing', ['nursedom', 'epidictical', 'defortify', 'taraf'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
    'epidictical'
    >>> autocorrect('corvina', ['predivinable', 'buchnerite', 'unexplanatory', 'nisei', 'neuronophagia', 'geitjie', 'porticoed', 'corvina'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'corvina'
    >>> autocorrect('nonreception', ['booming', 'retrothyroid', 'decarnate', 'lobbyism', 'playa', 'nonreception', 'amphictyonic', 'antiaesthetic', 'unjoyousness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'nonreception'
    >>> autocorrect('slopingness', ['toxone', 'nucleiform', 'priggish', 'intramuscularly', 'slopingness', 'saccharinated'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'slopingness'
    >>> autocorrect('cacoglossia', ['twankingly', 'eccentrate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
    'twankingly'
    >>> autocorrect('warriorwise', ['predigest', 'adipocellulose', 'warriorwise', 'sought', 'sciatherically', 'sexuale', 'onionlike'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
    'warriorwise'
    >>> autocorrect('unpretendingly', ['unpretendingly', 'puppydom', 'lardworm', 'equestrianship', 'semolella', 'pauperize', 'athericeran', 'receipt', 'nonrevelation', 'pomacentroid'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'unpretendingly'
    >>> autocorrect('antagony', ['devisable', 'mountainet', 'swoony'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'devisable'
    >>> autocorrect('escadrille', ['statolatry', 'bossism', 'latitudinal', 'stringless', 'hypsobathymetric', 'coinfinity', 'autotype', 'figurant'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'statolatry'
    >>> autocorrect('anoplocephalic', ['grovel', 'stethoscopy', 'suddenty', 'legislatively', 'anoplocephalic', 'unimportant', 'unplace', 'plouk', 'crossed'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'anoplocephalic'
    >>> autocorrect('demipauldron', ['inclose', 'indistinctness', 'schemata', 'staying', 'volvent', 'snaringly', 'unflat', 'unruminatingly', 'plurisyllable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'demipauldron'
    >>> autocorrect('hexametrical', ['unbraceleted', 'runner', 'nickeline', 'cellulous', 'interlocutorily', 'ophthalmodynia', 'unthrone', 'pronunciability'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'unbraceleted'
    >>> autocorrect('deuteride', ['deuteride', 'mimiambic', 'isoimmunity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'deuteride'
    >>> autocorrect('pneumohydropericardium', ['spelunk', 'democratifiable', 'vacuous', 'spontaneous', 'supercapable', 'koolokamba', 'nosism', 'diplopia', 'biaxillary'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
    'pneumohydropericardium'
    >>> autocorrect('archsacrificer', ['complications', 'unprophetical', 'unrevoked', 'profugate', 'voltmeter', 'foregoneness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'complications'
    >>> autocorrect('pilgrimatical', ['cystolithic', 'orderly', 'stupidhead', 'valveless', 'miffiness', 'arrhenotoky', 'curiously', 'gerenuk', 'underbed'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
    'pilgrimatical'
    >>> autocorrect('artillery', ['chromophilic', 'brabant', 'detailed', 'exulcerative'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'detailed'
    >>> autocorrect('buncal', ['twixt', 'benzolize', 'ebenaceous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'twixt'
    >>> autocorrect('dichlorohydrin', ['myosarcomatous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'myosarcomatous'
    >>> autocorrect('vaulty', ['mastigopodous', 'fragileness', 'petulance'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
    'petulance'
    >>> autocorrect('demodectic', ['tribunitive', 'mungofa', 'demodectic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
    'demodectic'
    >>> autocorrect('intersperse', ['lighttight', 'nautilite', 'alastrim', 'acetosalicylic', 'omnigerent', 'divisiveness', 'transubstantiationite', 'macrocyst'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
    'lighttight'
    >>> autocorrect('pratfall', ['quinometry', 'tyste', 'schistosome', 'reinclude', 'noncounty', 'shirtwaist'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'reinclude'
    >>> autocorrect('bushful', ['actionary', 'pogonologist', 'snack', 'sabromin', 'hypervitalize', 'lakemanship', 'xylographical', 'barytone'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'sabromin'
    >>> autocorrect('undared', ['chorizontes', 'infuriate', 'huddledom', 'pertly', 'bisacromial', 'taihoa', 'eponymize', 'commiserator', 'lightness', 'displeasurement'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'undared'
    >>> autocorrect('tissue', ['plumbable', 'siroccoishly', 'uji', 'mortific', 'unbolt', 'loxodont', 'vasodilation', 'tartarize', 'tissue'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'tissue'
    >>> autocorrect('undulous', ['seedcase', 'rudder', 'muttering', 'individualize', 'undulous', 'adhamant'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'undulous'
    >>> autocorrect('mild', ['remittance', 'ropish', 'undetermined', 'sigillographical', 'nounally', 'ununiversitylike'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
    'ropish'
    >>> autocorrect('chrysobull', ['geophyte', 'menthenone', 'aerobatic', 'begrease', 'darklings', 'ropable', 'overcharity', 'fineleaf'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'menthenone'
    >>> autocorrect('upbelch', ['subchoroid', 'briefing'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
    'briefing'
    >>> autocorrect('neckful', ['denunciator', 'gemmate', 'brigade', 'secondariness', 'verification', 'counteridea'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
    'gemmate'
    >>> autocorrect('microblephary', ['retardant', 'preadequately'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
    'preadequately'
    >>> autocorrect('trophobiosis', ['trophobiosis'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'trophobiosis'
    >>> autocorrect('cate', ['graphics', 'cate', 'missuppose', 'decalvation'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'cate'
    >>> autocorrect('grue', ['synovitis', 'uninsultable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
    'grue'
    >>> autocorrect('urinogenital', ['intransigency', 'improperly', 'angiophorous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
    'angiophorous'
    >>> autocorrect('scarid', ['reticuloramose', 'pseudonymuncule', 'cacoepist', 'scarid', 'carbethoxyl', 'truncatorotund', 'unfelicitated', 'mochras'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'scarid'
    >>> autocorrect('gentilize', ['gentilize', 'trihemimeral', 'bifid'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'gentilize'
    >>> autocorrect('chemitypy', ['keratonyxis', 'chemitypy', 'checkroll', 'hymnographer', 'tootler', 'perithelium', 'monodelph', 'manualism', 'neuroglial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
    'chemitypy'
    >>> autocorrect('homoeopathician', ['woomerang', 'entempest', 'spratty', 'unabatingly', 'hemocyanin', 'scoptophilic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'homoeopathician'
    >>> autocorrect('unscared', ['unregimented', 'dissuasiveness', 'unissuable', 'soiling', 'connotative'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'soiling'
    >>> autocorrect('cottabus', ['cottabus', 'prescapularis', 'revaporization', 'censerless'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
    'cottabus'
    >>> autocorrect('preshipment', ['typolithographic', 'telephone', 'palatial', 'autocamper'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'preshipment'
    >>> autocorrect('catholicus', ['aestheticism', 'skullful', 'catholicus', 'headphone', 'fiend', 'lordy', 'sarlak', 'presuppositionless', 'squamulae'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'catholicus'
    >>> autocorrect('quadripartition', ['ingress', 'ungag'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
    'quadripartition'
    >>> autocorrect('nacrite', ['behavior', 'aberdevine', 'dd', 'isopetalous', 'rousting', 'nonmonarchist', 'backjoint', 'unhearing', 'notice'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'nacrite'
    >>> autocorrect('beast', ['borderlander', 'vedette', 'uncleverness', 'approaches', 'moviedom'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'vedette'
    >>> autocorrect('presidence', ['bipupillate', 'gilbert', 'cardiagra'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
    'presidence'
    >>> autocorrect('dynamic', ['dynamic', 'twistable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
    'dynamic'
    >>> autocorrect('pungey', ['toxicodermatitis', 'gallification', 'survival', 'rakshasa', 'pungey', 'overgrossness', 'postconvalescent', 'gander'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
    'pungey'
    >>> autocorrect('clouding', ['cacomixle', 'endonuclear', 'writer'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'cacomixle'
    >>> autocorrect('losing', ['losing'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'losing'
    >>> autocorrect('refederate', ['subframe', 'infinitude', 'astrochemist', 'shoulderer', 'sensation', 'nuclide', 'hallelujah'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
    'infinitude'
    >>> autocorrect('coolie', ['overusually', 'supercargoship', 'contemptuous', 'undrawn', 'catchpollery', 'unfinishedness', 'coolie', 'siruaballi', 'tsia'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
    'coolie'
    >>> autocorrect('chico', ['define', 'unmudded', 'unnourishing', 'fendable', 'spherulitize'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
    'define'
    >>> autocorrect('cointersecting', ['ungenuine', 'dealable', 'pejorism'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'ungenuine'
    >>> autocorrect('does', ['sulphamidic', 'monopersulfuric', 'heartsickening', 'talkathon', 'does', 'beveil', 'aeroperitoneum'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
    'does'
    >>> autocorrect('bullation', ['angiography', 'nonsidereal', 'bullation'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
    'bullation'
    >>> autocorrect('unclement', ['disdiapason', 'unclement', 'cesser', 'repatronize', 'sacerdotalist'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
    'unclement'
    """
