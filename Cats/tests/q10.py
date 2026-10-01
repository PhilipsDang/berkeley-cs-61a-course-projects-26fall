from pytest_grader import points


@points(0)
def fastest_words():
    r"""
    >>> from cats import fastest_words, get_time
    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 2]
    >>> get_time([p0, p1], 0, 1)
    LOCKED: 8f27f63414bf59fb
    >>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1]})
    LOCKED: 7eeac0b091294663
    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 3]
    >>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1]})  # with a tie, choose the first player
    LOCKED: 228ab0a082c007f5
    >>> p2 = [4, 3, 1]
    >>> fastest_words({'words': ['What', 'great', 'luck'], 'times': [p0, p1, p2]})
    LOCKED: 5f578c7fe0c128e1
    """


@points(3)
def fastest_words_examples():
    r"""
    >>> from cats import fastest_words, get_time
    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [p0, p1]})
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    >>> p = [[3], [5]]
    >>> fastest_words({'words': ['smopple'], 'times': p})
    [['smopple'], []]
    >>> p = [[]]
    >>> fastest_words({'words': [], 'times': p})
    [[]]
    >>> p = [[5], [2], [4]]
    >>> fastest_words({'words': ['seeingly'], 'times': p})
    [[], ['seeingly'], []]
    >>> p = [[4, 1, 2, 3, 4], [1, 5, 3, 4, 1], [5, 1, 5, 2, 3]]
    >>> fastest_words({'words': ['reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary'], 'times': p})
    [['unweld', 'handgun'], ['reundergo', 'recessionary'], ['hydrometra']]
    >>> p = [[], [], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], [], []]
    >>> p = [[2, 1, 2]]
    >>> fastest_words({'words': ['prebeleve', 'upanishadic', 'ftp'], 'times': p})
    [['prebeleve', 'upanishadic', 'ftp']]
    >>> p = [[5, 3, 5, 2, 4], [2, 4, 5, 1, 2], [1, 5, 2, 1, 3]]
    >>> fastest_words({'words': ['supplies', 'underivedly', 'henter', 'undeserving', 'uncope'], 'times': p})
    [['underivedly'], ['undeserving', 'uncope'], ['supplies', 'henter']]
    >>> p = [[], [], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], [], []]
    >>> p = [[1, 5, 5, 5, 5]]
    >>> fastest_words({'words': ['pentarch', 'nihilification', 'krieker', 'laureate', 'antechamber'], 'times': p})
    [['pentarch', 'nihilification', 'krieker', 'laureate', 'antechamber']]
    >>> p = [[3, 4, 4, 3, 4]]
    >>> fastest_words({'words': ['urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation'], 'times': p})
    [['urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation']]
    >>> p = [[2, 4, 1, 1, 4, 1], [5, 3, 3, 4, 5, 3], [1, 2, 3, 1, 3, 5]]
    >>> fastest_words({'words': ['isoborneol', 'glabrate', 'excision', 'octobass', 'prevolitional', 'archtreasurership'], 'times': p})
    [['excision', 'octobass', 'archtreasurership'], [], ['isoborneol', 'glabrate', 'prevolitional']]
    >>> p = [[5, 2, 4, 3, 1], [3, 1, 2, 1, 3]]
    >>> fastest_words({'words': ['singletree', 'apocyneous', 'imminution', 'uncensuring', 'fungiform'], 'times': p})
    [['fungiform'], ['singletree', 'apocyneous', 'imminution', 'uncensuring']]
    >>> p = [[], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], []]
    >>> p = [[]]
    >>> fastest_words({'words': [], 'times': p})
    [[]]
    >>> p = [[1, 2], [3, 2]]
    >>> fastest_words({'words': ['snideness', 'universalization'], 'times': p})
    [['snideness', 'universalization'], []]
    >>> p = [[1], [3]]
    >>> fastest_words({'words': ['dependably'], 'times': p})
    [['dependably'], []]
    >>> p = [[3, 2, 1]]
    >>> fastest_words({'words': ['spaceful', 'cautery', 'wiseness'], 'times': p})
    [['spaceful', 'cautery', 'wiseness']]
    >>> p = [[3, 4, 5, 3, 5, 1], [4, 4, 1, 2, 5, 3]]
    >>> fastest_words({'words': ['investigatable', 'quadrigenarious', 'protonemal', 'cardiodysneuria', 'provoker', 'associated'], 'times': p})
    [['investigatable', 'quadrigenarious', 'provoker', 'associated'], ['protonemal', 'cardiodysneuria']]
    >>> p = [[5, 1]]
    >>> fastest_words({'words': ['tubuliporoid', 'malleability'], 'times': p})
    [['tubuliporoid', 'malleability']]
    >>> p = [[4, 1, 2, 4, 4], [3, 4, 3, 3, 5], [1, 2, 5, 1, 2]]
    >>> fastest_words({'words': ['shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright'], 'times': p})
    [['shrubbiness', 'demoded'], [], ['shilling', 'commentary', 'housewright']]
    >>> p = [[3, 3, 3, 4, 1]]
    >>> fastest_words({'words': ['ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular'], 'times': p})
    [['ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular']]
    >>> p = [[4, 1, 4, 3, 1], [5, 5, 1, 2, 3]]
    >>> fastest_words({'words': ['lithosis', 'bogland', 'interclash', 'widespread', 'thumbbird'], 'times': p})
    [['lithosis', 'bogland', 'thumbbird'], ['interclash', 'widespread']]
    >>> p = [[1, 2], [3, 3]]
    >>> fastest_words({'words': ['diplosphenal', 'cholecystogram'], 'times': p})
    [['diplosphenal', 'cholecystogram'], []]
    >>> p = [[1, 2]]
    >>> fastest_words({'words': ['eugenist', 'karyopyknosis'], 'times': p})
    [['eugenist', 'karyopyknosis']]
    >>> p = [[5, 4, 3]]
    >>> fastest_words({'words': ['cannily', 'lune', 'heathless'], 'times': p})
    [['cannily', 'lune', 'heathless']]
    >>> p = [[4, 4, 3, 3], [2, 1, 3, 4], [2, 2, 4, 4]]
    >>> fastest_words({'words': ['postprandially', 'helicogyrate', 'coccidology', 'circumradius'], 'times': p})
    [['coccidology', 'circumradius'], ['postprandially', 'helicogyrate'], []]
    >>> p = [[2, 3], [1, 3], [5, 1]]
    >>> fastest_words({'words': ['electrofused', 'incontinent'], 'times': p})
    [[], ['electrofused'], ['incontinent']]
    >>> p = [[], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], []]
    >>> p = [[]]
    >>> fastest_words({'words': [], 'times': p})
    [[]]
    >>> p = [[], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], []]
    >>> p = [[2, 3, 2, 5, 3], [3, 3, 5, 5, 3]]
    >>> fastest_words({'words': ['trigon', 'effluviate', 'unhuman', 'energeia', 'slouch'], 'times': p})
    [['trigon', 'effluviate', 'unhuman', 'energeia', 'slouch'], []]
    >>> p = [[]]
    >>> fastest_words({'words': [], 'times': p})
    [[]]
    >>> p = [[3, 1, 1, 1, 2], [1, 1, 5, 3, 4]]
    >>> fastest_words({'words': ['boucherism', 'rutabaga', 'fomentation', 'swampside', 'unpopularness'], 'times': p})
    [['rutabaga', 'fomentation', 'swampside', 'unpopularness'], ['boucherism']]
    >>> p = [[2, 1], [1, 2]]
    >>> fastest_words({'words': ['introspectionist', 'teeting'], 'times': p})
    [['teeting'], ['introspectionist']]
    >>> p = [[1, 3, 1, 2, 3, 3]]
    >>> fastest_words({'words': ['cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient'], 'times': p})
    [['cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient']]
    >>> p = [[4, 4, 2, 2, 3], [1, 2, 5, 1, 3]]
    >>> fastest_words({'words': ['quodlibetic', 'previdence', 'nonviscous', 'reduplicatively', 'arterioverter'], 'times': p})
    [['nonviscous', 'arterioverter'], ['quodlibetic', 'previdence', 'reduplicatively']]
    >>> p = [[1, 2, 5, 1, 2, 1], [4, 2, 1, 4, 5, 3]]
    >>> fastest_words({'words': ['cactoid', 'quadrialate', 'preflattery', 'emancipation', 'recedent', 'haustement'], 'times': p})
    [['cactoid', 'quadrialate', 'emancipation', 'recedent', 'haustement'], ['preflattery']]
    >>> p = [[4, 1, 5, 4, 4, 4], [5, 2, 1, 1, 2, 3], [4, 5, 4, 2, 3, 2]]
    >>> fastest_words({'words': ['puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous', 'phycomycete'], 'times': p})
    [['puboprostatic', 'tumescent'], ['keraunograph', 'telecaster', 'selenigenous'], ['phycomycete']]
    >>> p = [[2, 4, 2, 4, 2], [1, 5, 1, 4, 5]]
    >>> fastest_words({'words': ['indisputableness', 'breastrope', 'hypocist', 'supersemination', 'ethnographically'], 'times': p})
    [['breastrope', 'supersemination', 'ethnographically'], ['indisputableness', 'hypocist']]
    >>> p = [[5, 4, 3, 3, 5, 4]]
    >>> fastest_words({'words': ['repetitiously', 'lecideiform', 'debtless', 'stream', 'loquent', 'leery'], 'times': p})
    [['repetitiously', 'lecideiform', 'debtless', 'stream', 'loquent', 'leery']]
    >>> p = [[4, 3, 3, 3, 1, 4]]
    >>> fastest_words({'words': ['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations'], 'times': p})
    [['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations']]
    >>> p = [[2, 2, 5, 4], [5, 4, 2, 2]]
    >>> fastest_words({'words': ['holland', 'nursedom', 'epidictical', 'defortify'], 'times': p})
    [['holland', 'nursedom'], ['epidictical', 'defortify']]
    >>> p = [[3, 1, 3]]
    >>> fastest_words({'words': ['sunbird', 'renewal', 'predivinable'], 'times': p})
    [['sunbird', 'renewal', 'predivinable']]
    >>> p = [[]]
    >>> fastest_words({'words': [], 'times': p})
    [[]]
    >>> p = [[]]
    >>> fastest_words({'words': [], 'times': p})
    [[]]
    >>> p = [[1, 3, 4, 2], [5, 2, 2, 3]]
    >>> fastest_words({'words': ['tillot', 'douser', 'twankingly', 'eccentrate'], 'times': p})
    [['tillot', 'eccentrate'], ['douser', 'twankingly']]
    >>> p = [[4, 4, 5, 3]]
    >>> fastest_words({'words': ['reest', 'predigest', 'adipocellulose', 'warriorwise'], 'times': p})
    [['reest', 'predigest', 'adipocellulose', 'warriorwise']]
    >>> p = [[5, 1, 5, 3, 5]]
    >>> fastest_words({'words': ['standing', 'cameroon', 'unpretendingly', 'puppydom', 'lardworm'], 'times': p})
    [['standing', 'cameroon', 'unpretendingly', 'puppydom', 'lardworm']]
    >>> p = [[], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], []]
    >>> p = [[1, 4], [5, 5]]
    >>> fastest_words({'words': ['cardioarterial', 'statolatry'], 'times': p})
    [['cardioarterial', 'statolatry'], []]
    >>> p = [[1, 5, 4, 1]]
    >>> fastest_words({'words': ['whirley', 'coldly', 'compendiary', 'grovel'], 'times': p})
    [['whirley', 'coldly', 'compendiary', 'grovel']]
    >>> p = [[2, 1], [3, 3], [2, 4]]
    >>> fastest_words({'words': ['caducicorn', 'monociliated'], 'times': p})
    [['caducicorn', 'monociliated'], [], []]
    >>> p = [[], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], []]
    >>> p = [[2, 3, 4, 5, 3]]
    >>> fastest_words({'words': ['audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx'], 'times': p})
    [['audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx']]
    >>> p = [[5], [4], [4]]
    >>> fastest_words({'words': ['millage'], 'times': p})
    [[], ['millage'], []]
    >>> p = [[3, 1], [5, 4]]
    >>> fastest_words({'words': ['inyoite', 'complications'], 'times': p})
    [['inyoite', 'complications'], []]
    >>> p = [[2, 2], [2, 2], [4, 1]]
    >>> fastest_words({'words': ['sarcodous', 'microbiological'], 'times': p})
    [['sarcodous'], [], ['microbiological']]
    >>> p = [[4, 4, 1], [2, 2, 3]]
    >>> fastest_words({'words': ['chromophilic', 'brabant', 'detailed'], 'times': p})
    [['detailed'], ['chromophilic', 'brabant']]
    >>> p = [[], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], []]
    >>> p = [[4, 1, 1, 1], [3, 1, 3, 3]]
    >>> fastest_words({'words': ['allochiral', 'hear', 'snur', 'myosarcomatous'], 'times': p})
    [['hear', 'snur', 'myosarcomatous'], ['allochiral']]
    >>> p = [[2], [5]]
    >>> fastest_words({'words': ['studiedly'], 'times': p})
    [['studiedly'], []]
    >>> p = [[3, 3, 3, 5, 2, 5]]
    >>> fastest_words({'words': ['katatonia', 'myoporaceous', 'tribunitive', 'mungofa', 'demodectic', 'kolobion'], 'times': p})
    [['katatonia', 'myoporaceous', 'tribunitive', 'mungofa', 'demodectic', 'kolobion']]
    >>> p = [[], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], []]
    >>> p = [[5, 2], [2, 2]]
    >>> fastest_words({'words': ['cheeser', 'cumulation'], 'times': p})
    [['cumulation'], ['cheeser']]
    >>> p = [[2, 2], [1, 3]]
    >>> fastest_words({'words': ['overemphatic', 'telpherway'], 'times': p})
    [['telpherway'], ['overemphatic']]
    >>> p = [[4, 4], [1, 2], [3, 5]]
    >>> fastest_words({'words': ['ultradolichocephalic', 'kinetophone'], 'times': p})
    [[], ['ultradolichocephalic', 'kinetophone'], []]
    >>> p = [[4, 5, 3]]
    >>> fastest_words({'words': ['protosaurian', 'plumbable', 'siroccoishly'], 'times': p})
    [['protosaurian', 'plumbable', 'siroccoishly']]
    >>> p = [[1, 5, 4, 5, 1, 1]]
    >>> fastest_words({'words': ['hydroidean', 'pesterer', 'seedcase', 'rudder', 'muttering', 'individualize'], 'times': p})
    [['hydroidean', 'pesterer', 'seedcase', 'rudder', 'muttering', 'individualize']]
    >>> p = [[3, 2, 1, 2], [2, 3, 5, 3]]
    >>> fastest_words({'words': ['oleostearin', 'stitching', 'theanthropism', 'blate'], 'times': p})
    [['stitching', 'theanthropism', 'blate'], ['oleostearin']]
    >>> p = [[1, 1], [2, 2]]
    >>> fastest_words({'words': ['oscillatory', 'geophyte'], 'times': p})
    [['oscillatory', 'geophyte'], []]
    >>> p = [[1], [2]]
    >>> fastest_words({'words': ['withsave'], 'times': p})
    [['withsave'], []]
    >>> p = [[5, 1, 1], [5, 3, 4]]
    >>> fastest_words({'words': ['battlewise', 'dare', 'halibiu'], 'times': p})
    [['battlewise', 'dare', 'halibiu'], []]
    >>> p = [[3, 1, 4, 2], [4, 3, 5, 5]]
    >>> fastest_words({'words': ['muscoid', 'reliquidation', 'broad', 'tugging'], 'times': p})
    [['muscoid', 'reliquidation', 'broad', 'tugging'], []]
    >>> p = [[4, 2, 5]]
    >>> fastest_words({'words': ['trophobiosis', 'parascenium', 'gibbet'], 'times': p})
    [['trophobiosis', 'parascenium', 'gibbet']]
    >>> p = [[1, 1, 4]]
    >>> fastest_words({'words': ['nonsparking', 'calool', 'dorsopleural'], 'times': p})
    [['nonsparking', 'calool', 'dorsopleural']]
    >>> p = [[2, 4], [4, 4], [5, 3]]
    >>> fastest_words({'words': ['unexcusableness', 'bismuthyl'], 'times': p})
    [['unexcusableness'], [], ['bismuthyl']]
    >>> p = [[5, 4, 5, 5, 2], [1, 4, 1, 2, 4]]
    >>> fastest_words({'words': ['evolution', 'intransigency', 'improperly', 'angiophorous', 'urinogenital'], 'times': p})
    [['intransigency', 'urinogenital'], ['evolution', 'improperly', 'angiophorous']]
    >>> p = [[5, 5, 1]]
    >>> fastest_words({'words': ['penceless', 'bromothymol', 'reticuloramose'], 'times': p})
    [['penceless', 'bromothymol', 'reticuloramose']]
    >>> p = [[1, 4, 5, 2, 2, 3]]
    >>> fastest_words({'words': ['monument', 'appressor', 'tutu', 'gentilize', 'trihemimeral', 'bifid'], 'times': p})
    [['monument', 'appressor', 'tutu', 'gentilize', 'trihemimeral', 'bifid']]
    >>> p = [[1, 4, 3, 3, 5, 2]]
    >>> fastest_words({'words': ['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer'], 'times': p})
    [['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer']]
    >>> p = [[2], [4], [3]]
    >>> fastest_words({'words': ['inclementness'], 'times': p})
    [['inclementness'], [], []]
    >>> p = [[], []]
    >>> fastest_words({'words': [], 'times': p})
    [[], []]
    >>> p = [[5, 1, 3, 1, 2, 4]]
    >>> fastest_words({'words': ['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis'], 'times': p})
    [['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis']]
    >>> p = [[4], [5], [4]]
    >>> fastest_words({'words': ['transmundane'], 'times': p})
    [['transmundane'], [], []]
    >>> p = [[1, 3]]
    >>> fastest_words({'words': ['becense', 'hyperingenuity'], 'times': p})
    [['becense', 'hyperingenuity']]
    >>> p = [[5, 3, 4], [5, 5, 3], [3, 2, 3]]
    >>> fastest_words({'words': ['interventional', 'demiditone', 'chrysophilite'], 'times': p})
    [[], ['chrysophilite'], ['interventional', 'demiditone']]
    >>> p = [[2, 5, 3, 5, 1, 3], [1, 4, 3, 1, 3, 4], [1, 3, 1, 4, 4, 5]]
    >>> fastest_words({'words': ['pyritology', 'marbleize', 'blooddrop', 'prickingly', 'ecole', 'capitellar'], 'times': p})
    [['ecole', 'capitellar'], ['pyritology', 'prickingly'], ['marbleize', 'blooddrop']]
    >>> p = [[3, 5, 4, 5, 4, 3], [1, 3, 1, 1, 3, 5]]
    >>> fastest_words({'words': ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious', 'untakableness'], 'times': p})
    [['untakableness'], ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious']]
    >>> p = [[2, 3], [4, 3], [5, 5]]
    >>> fastest_words({'words': ['tutoyer', 'fibrilliferous'], 'times': p})
    [['tutoyer', 'fibrilliferous'], [], []]
    >>> p = [[1, 2, 2, 1]]
    >>> fastest_words({'words': ['aneuploidy', 'unrubified', 'dynamic', 'twistable'], 'times': p})
    [['aneuploidy', 'unrubified', 'dynamic', 'twistable']]
    >>> p = [[2, 2, 2, 3]]
    >>> fastest_words({'words': ['pholadoid', 'toxicodermatitis', 'gallification', 'survival'], 'times': p})
    [['pholadoid', 'toxicodermatitis', 'gallification', 'survival']]
    >>> p = [[3, 3, 1, 4, 5], [5, 2, 3, 2, 3]]
    >>> fastest_words({'words': ['principiate', 'archinfamy', 'cacomixle', 'endonuclear', 'writer'], 'times': p})
    [['principiate', 'cacomixle'], ['archinfamy', 'endonuclear', 'writer']]
    >>> p = [[5, 5, 2, 4]]
    >>> fastest_words({'words': ['mechanicalist', 'losing', 'emancipation', 'counterquarterly'], 'times': p})
    [['mechanicalist', 'losing', 'emancipation', 'counterquarterly']]
    >>> p = [[4, 5, 1], [2, 1, 3]]
    >>> fastest_words({'words': ['subframe', 'infinitude', 'astrochemist'], 'times': p})
    [['astrochemist'], ['subframe', 'infinitude']]
    >>> p = [[2]]
    >>> fastest_words({'words': ['isocheimal'], 'times': p})
    [['isocheimal']]
    >>> p = [[1, 4, 4, 5], [5, 4, 5, 2]]
    >>> fastest_words({'words': ['mistresshood', 'lazzarone', 'define', 'unmudded'], 'times': p})
    [['mistresshood', 'lazzarone', 'define'], ['unmudded']]
    >>> p = [[4, 5, 2, 2, 4], [3, 5, 4, 5, 1]]
    >>> fastest_words({'words': ['either', 'ungenuine', 'dealable', 'pejorism', 'cointersecting'], 'times': p})
    [['ungenuine', 'dealable', 'pejorism'], ['either', 'cointersecting']]
    >>> p = [[2, 1]]
    >>> fastest_words({'words': ['narcoanesthesia', 'tanbur'], 'times': p})
    [['narcoanesthesia', 'tanbur']]
    >>> p = [[]]
    >>> fastest_words({'words': [], 'times': p})
    [[]]
    >>> p = [[1, 4]]
    >>> fastest_words({'words': ['overappraise', 'disdiapason'], 'times': p})
    [['overappraise', 'disdiapason']]
    """
