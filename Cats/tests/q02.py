from pytest_grader import points


@points(0)
def about():
    r"""
    >>> from cats import about
    >>> from cats import pick
    >>> dogs = about(['dogs', 'hounds'])
    >>> dogs('A passage about cats.')
    LOCKED: 34ad2e9b2a10559b
    >>> dogs('A passage about dogs.')
    LOCKED: c47da038787a4f36
    >>> dogs('Release the Hounds!')
    LOCKED: 703f5085b589f87f
    >>> dogs('"DOGS" stands for Department Of Geophysical Science.')
    LOCKED: 5aba7be20031f568
    >>> dogs('Do gs and ho unds don\'t count')
    LOCKED: 41baa28d085ddf20
    >>> dogs("AdogsPassage")
    LOCKED: 87fde020b0deea0d
    """


@points(1)
def about_examples():
    r"""
    >>> from cats import about
    >>> from cats import pick
    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    >>> from cats import about
    >>> ab = about(['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly', 'cloaklet'])
    >>> ab('unhollow simsim dcloakletB itinerantly cloakLet dQUaNtivalentJ gnEurinE fissiparity Mneurinel')
    True
    >>> ab = about(['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement', 'neomorph'])
    >>> ab('#crystallogenIcalW podded reorganizationist neomorPhf hneomorphj')
    False
    >>> ab = about(['smopple', 'modernizer'])
    >>> ab('tongsman smopplek ASmoppleg Bsm(<opPLeF SMopPlES')
    False
    >>> ab = about(['equalizing', 'phrymaceous', 'fluidimeter', 'seeds', 'bridgemaking'])
    >>> ab('xph+rymaceous hobbledehoyism zphrymaceousy ofluidimeter Lseeds?\\ interbank DsEe)dS consumer iatromathematical')
    False
    >>> ab = about(['seeingly', 'essexite'])
    >>> ab('essexite clupeine habeas disrupture faceable phototypography LseeIngly seeingly')
    True
    >>> ab = about(['probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary', 'grippotoxin'])
    >>> ab('DreuNdergo reundergo unabAtedlYM grippotoxin Lre<und!ergoy')
    True
    >>> ab = about(['elysia'])
    >>> ab('hewlett el=ysiA` pamphletic elysia te#Lysiac')
    True
    >>> ab = about(['entomical'])
    >>> ab('obduction polyacid en\\tomical{w entoMicAlP entO[m]icalP befrill zentom[icalr centomi_CAl')
    False
    >>> ab = about(['choirwise', 'uncircumstantial', 'glassine', 'supplies', 'underivedly', 'henter', 'undeserving', 'uncope'])
    >>> ab('tazia uncope glassine glassineW eChoirwis<e& uncircumstaNTIal uninventiveness pentahexahedral')
    True
    >>> ab = about(['epinaos', 'unpresented', 'homotypic'])
    >>> ab('coenoecial synodist tipper unportentous sclerometer epinaos unpresented catnip homotypicy')
    True
    >>> ab = about(['cuir'])
    >>> ab('cuir polystomatous illiterately Hc)uI`re cCuir jc|ui!R cUir CUirG barycentric')
    True
    >>> ab = about(['enterohelcosis', 'urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation', 'peepeye', 'nonuterine', 'antilacrosse'])
    >>> ab('enteRoh<eLcos:ise peepeyep misappreciation enteROhel<co]sis CSporoid peepeyel desoxybenzoin')
    True
    >>> ab = about(['excision', 'octobass', 'prevolitional', 'archtreasurership', 'metadiazine', 'overwomanize'])
    >>> ab('Larchtreasurershipk octobass carder handclasp O`exCiSion ,excisiont scavenger')
    True
    >>> ab = about(['nailless', 'singletree'])
    >>> ab('qualificator accoy crystallogeny players clubfellow')
    False
    >>> ab = about(['nonexpiry', 'toywoman', 'impercipient', 'overrude', 'hyperingenuity', 'piligerous', 'molybdocolic', 'toxicum', 'testator'])
    >>> ab('nonexpiryV testator piligerous noNe,xpiry reconcentrate smolybdocolick')
    True
    >>> ab = about(['misinstruction', 'durian', 'underriding', 'chillroom', 'unabsorb', 'chromolithographic', 'hemadynamometer', 'frailly', 'diana'])
    >>> ab('dodoism wmisinstruction ghemadYnamomeTerg euphonious funderridin!Gm')
    False
    >>> ab = about(['snideness', 'universalization', 'accroach'])
    >>> ab('crock omophagous testamentate Aa=CcroacH<n AccROaChS')
    False
    >>> ab = about(['hecatontome', 'glioma', 'dispiteousness', 'dependably'])
    >>> ab('Cd?ependab_ly adipocere ngliomaE glioMaV vigor dispiteousness')
    True
    >>> ab = about(['spaceful', 'cautery', 'wiseness', 'yobi'])
    >>> ab('SwiSenesS* chavicin wisene]ss}z embryoma Tsp|!acefUl')
    False
    >>> ab = about(['hemicranic', 'hieromachy', 'investigatable', 'quadrigenarious', 'protonemal', 'cardiodysneuria', 'provoker', 'associated'])
    >>> ab('quadrigenariousE Lpro-tonemalz mesorchial Ohierom]achyh dinveStigatable f')
    False
    >>> ab = about(['tubuliporoid', 'malleability', 'scusation'])
    >>> ab('RtubuLiporoiDA Dmalleability mAlLeabilit@yi malleabilIty scusAtioN bmalleability josh')
    True
    >>> ab = about(['shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright', 'sinusoid'])
    >>> ab('ridgepoled halogen sclerometric sclerochoroiditis odemodEdi opercle')
    False
    >>> ab = about(['beydom', 'ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular', 'recuperator', 'goto', 'turnsole'])
    >>> ab('JrEcupeRatorJ ZgotO t|urnsoLe#K re#cuperatoRZ tAngleproOfu mmultiVincularl ibeydom beydomG')
    False
    >>> ab = about(['lithosis', 'bogland', 'interclash', 'widespread', 'thumbbird', 'gymnophiona'])
    >>> ab('CI$nteRc{lash KthumbbirdI FlithosiS crinigerous ElithoSis vthumbBird')
    False
    >>> ab = about(['diplosphenal', 'cholecystogram', 'maximization'])
    >>> ab('diplosphenal cholecYstogramC otherhow gaulin Cmaxim}izaTio]nU fatuism cholecystogram maximization')
    True
    >>> ab = about(['metatatic', 'eugenist', 'karyopyknosis', 'nightwork', 'short', 'insee', 'unmated', 'capacitation', 'constructivist'])
    >>> ab('constructivist dnigHt-woR=kn WnighTworkd o\\k~aryopyknoSis karyopyknosis unrepresentative imetata(tic kaRy&opyknosis ichneumonized')
    True
    >>> ab = about(['distressedly', 'gibbet', 'cannily', 'lune'])
    >>> ab('luneW sesquitertia Wlune fluvioterrestrial wdistressedlyI')
    False
    >>> ab = about(['triplocaulescent', 'postprandially', 'helicogyrate', 'coccidology', 'circumradius', 'repairer', 'passingly'])
    >>> ab('triplocaulescent VtriplocaulescentF postprandially coccidology ccocciDoloGyw bloated ttriplocaulescent ncoccidology repaiRerN')
    True
    >>> ab = about(['electrofused', 'incontinent', 'activize'])
    >>> ab('assart acTi^vI]zeX unsulphonated activizep aincontinent Me}leCtrofused incontinent electrofused dactivized')
    True
    >>> ab = about(['unhabitableness'])
    >>> ab('arisen fibrochondroma afflatus drowsiness untopped unberth')
    False
    >>> ab = about(['tetragynian', 'persistently', 'becolme', 'seafare', 'bimillennium', 'valviform', 'thyridial', 'umbones', 'logitech'])
    >>> ab('bi$millenNIu"mx XThyridial unpunishable predeprivation PersiSteNtLy')
    True
    >>> ab = about(['unwarrant'])
    >>> ab('unWarrantx resort Junwarran<$TI unwarrantE subdepot reaggravation unwarrant')
    True
    >>> ab = about(['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia', 'slouch'])
    >>> ab('tRigOnz sinfoniEtta trigon trichotomism benergeian lsinfonietta bullsucker effluviate')
    True
    >>> ab = about(['tablespoon', 'anytime', 'ungotten', 'periostracal', 'laparogastrotomy', 'nucleonics', 'diaclase', 'wadmaking'])
    >>> ab('risen tablespoonS bichord coumarinic e]tablespoon')
    False
    >>> ab = about(['boucherism', 'rutabaga'])
    >>> ab('initiate boucherism baniya gnomological wirable superincumbently bouchEri(smg')
    True
    >>> ab = about(['pyranyl', 'uncertainty', 'nl', 'introspectionist', 'teeting', 'unbroiled', 'plumosity', 'restock'])
    >>> ab('Ynl nlS restockM Rnl_ r\\unbroiledH')
    False
    >>> ab = about(['dugong', 'cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient', 'ritelessness', 'blastoporal'])
    >>> ab('zinexpediEntV Nritele/ssnessA schizocarp PblAsToporal unluxurious')
    False
    >>> ab = about(['quodlibetic', 'previdence', 'nonviscous', 'reduplicatively', 'arterioverter', 'discrepation'])
    >>> ab('Upr)eviDEnce unvigilant discrepatIon arterioverteR UreduplicativelyE OdiscrEpation di~scRepaTion nonviscous arterioverter')
    True
    >>> ab = about(['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation', 'recedent'])
    >>> ab('eema@nciPation{T holochroal recedent chewstick cac,t_oid h\\semipervi@Ous cac&toid eManciPatIonb Urece]denTn')
    True
    >>> ab = about(['puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous', 'phycomycete', 'executrix'])
    >>> ab("plastidular tUmesC]ent selen'igenousE tumescent selen<igE;nOuS")
    True
    >>> ab = about(['unsculptured', 'quagginess', 'indisputableness', 'breastrope'])
    >>> ab('uNSculp:tureDy IBreastrope FindispuTaBlenessz nbreastr]opea nubile')
    False
    >>> ab = about(['intraperitoneally'])
    >>> ab('leader shipbreaking nondidactic intraperitoneally intraperitOneallyh PIntraperito$neAllY sorgho Intraperi,toneallyp clerklike')
    True
    >>> ab = about(['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations', 'figent'])
    >>> ab('VFigentU uncommemorated cinchotine viceroy Odriftweed figen!ts zvictorylessQ Dillustrations')
    False
    >>> ab = about(['holland', 'nursedom', 'epidictical', 'defortify', 'taraf'])
    >>> ab('stomatal vep,iDIctica`l n]urS~eDom PepidICtic/a"lx defortify')
    True
    >>> ab = about(['vegasite'])
    >>> ab('vegaSitec vegasiteI forwarder drumheads Sveg<asiteT tannalbin')
    False
    >>> ab = about(['tularemia', 'booming', 'retrothyroid', 'decarnate', 'lobbyism', 'playa', 'nonreception', 'amphictyonic', 'antiaesthetic'])
    >>> ab('KtUlaremia Y{=booMing mlobBYIsm Tular?emiai jeremiad')
    False
    >>> ab = about(['metamerically'])
    >>> ab('slopingness quidnunc priggish nonimpartment drillmaster entreaty nucleiform unimprovableness')
    False
    >>> ab = about(['scrofulism', 'missile', 'tillot', 'douser', 'twankingly', 'eccentrate', 'cacoglossia', 'miss'])
    >>> ab("seccentrAteO dcaCoglossiaF C$acoglossi'AA cacoglossia galera")
    True
    >>> ab = about(['encourager'])
    >>> ab('stratagemical sizableness schnabel encouragerl mythopoeist EncOuragerD')
    False
    >>> ab = about(['unambiguously', 'standing', 'cameroon', 'unpretendingly', 'puppydom'])
    >>> ab('mousekin unambiguousl*y standing unAmbigUously fpUppyDoma')
    True
    >>> ab = about(['megascleric', 'devisable'])
    >>> ab('nephrorrhaphy cactiform loaferdom Umegascleric dividing Tmegas`cleric readoption devisableH')
    False
    >>> ab = about(['cardioarterial', 'statolatry', 'bossism'])
    >>> ab('intercounty ost$atolaT)ry statolatrym Tbos(sisMm unsignatured brunch ZcardioArterialF')
    False
    >>> ab = about(['dextrousness', 'whirley', 'coldly', 'compendiary', 'grovel'])
    >>> ab('pseudoglioma co@ldlyt N<dEXtrous@nEss dextrousnessx coetaneously hydroelectricity abstruse')
    False
    >>> ab = about(['plowfoot', 'caducicorn', 'monociliated'])
    >>> ab("sp'lowfOot ploW&fO.oT -{ploWfootL monOciliaTedp yplowfootA")
    True
    >>> ab = about(['plash', 'unbraceleted', 'runner', 'nickeline', 'cellulous', 'interlocutorily', 'ophthalmodynia', 'unthrone'])
    >>> ab('aophthalmodyn`i|a Wun.bRa.celEtedz nIckeline{g cunbrac<eletedY uNthroneX')
    False
    >>> ab = about(['sulphurage', 'audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx', 'refractively', 'nonseizure'])
    >>> ab('i~soimmUniTy no}nseizure\\ gi"soimmunitY nonseizure bastionary usulph<u}raGet InonseIzur}ez imimiamb+ic odeuTeride')
    True
    >>> ab = about(['whitecapper', 'uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography', 'eulamellibranch'])
    >>> ab('HydrostaticH IuncoNtestablE=R renverse millagEt fascicle')
    False
    >>> ab = about(['remissful', 'inyoite'])
    >>> ab('waterlogged subpeduncle warriorhood Riny@oit,e wremis]sfUlm')
    False
    >>> ab = about(['microbiological', 'ruddy', 'gobble', 'pozzuolana', 'adscript', 'ossypite'])
    >>> ab('superadmiration ossypite nossy$pite adsCriptZ %gobble% pozzuolanau untempted')
    True
    >>> ab = about(['chromophilic', 'brabant', 'detailed', 'exulcerative', 'artillery', 'tachylytic', 'sinnable', 'clival'])
    >>> ab('ITac/hylytic snavvle Jchro%moPhili<cJ boundedly artil{lery treacherousness Fsi@~nnablEh')
    True
    >>> ab = about(['bounteousness', 'unimperious', 'twixt', 'benzolize', 'ebenaceous', 'buncal', 'cladoptosis', 'archvampire', 'palaeontographical'])
    >>> ab('polariscopy unimperIousH cLa]dop&tosisk Pbenz]oli>ze frigatoon EebEnaceousw Barchvampire floorer')
    False
    >>> ab = about(['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous', 'dichlorohydrin'])
    >>> ab('shakefork kh<ea$rq bromine ldichlor$ohydrIN snU,rb qhea|r sN-urX dhe>{Ar rdIchlorohydrin')
    False
    >>> ab = about(['sulphurproof', 'studiedly'])
    >>> ab('solifluctional knowledgeably Hsulphurproof denationalization studiedly polyphyletic')
    True
    >>> ab = about(['zygosporophore'])
    >>> ab('metrosteresis malconduct married semiform gangling szygoSporOpho,rek underdraft')
    False
    >>> ab = about(['detinet'])
    >>> ab('omnigerent alastrim acetosalicylic intersperse detinet macrocyst pathogermic')
    True
    >>> ab = about(['monarchize', 'prankster', 'egomaniacal', 'deediness', 'cheeser', 'cumulation', 'endorsee', 'quinometry'])
    >>> ab('jMon.archizeF ]egoManiacalW leucoplastid cumulatioNw localizable')
    False
    >>> ab = about(['varicosed', 'ventilator'])
    >>> ab('eventIlatorN Cvaricosedd reask ventil]atorb filiform Lvaricosed queak resinol')
    False
    >>> ab = about(['ultradolichocephalic', 'kinetophone', 'supernaturalness'])
    >>> ab('mesepithelial zkinetophone Oultra@Dolichocephalic ultrAdoLichocephaLicS tendant')
    False
    >>> ab = about(['somatoplasm'])
    >>> ab('heartlet JsomAtoplasmT somatoplasm jigginess xanthophane wader tuttiman diabrosis')
    True
    >>> ab = about(['trackback'])
    >>> ab('protiston asimmer vtraCkb-aCk imported trackback')
    True
    >>> ab = about(['payable', 'jaunt', 'oleostearin', 'stitching'])
    >>> ab('payablez feignedness kjaunt IstitchiNgO sti<tchin/gV')
    False
    >>> ab = about(['oscillatory', 'geophyte', 'menthenone'])
    >>> ab('Men*tH:enoney menthenone stalagmite conductometric assorter bardic')
    True
    >>> ab = about(['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch', 'plessimetric'])
    >>> ab('filterableness KsubchoRoid StookieN bri[efingH hornyhead dragonlike')
    False
    >>> ab = about(['battlewise', 'dare'])
    >>> ab('sulphanilic chondrosis dar<e FDare Ab}attlewi+seb')
    True
    >>> ab = about(['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant', 'preadequately'])
    >>> ab('retarDAnt _muscoi+DY preaDEquAtely tugging disarticulation')
    True
    >>> ab = about(['hexatomic', 'trophobiosis', 'parascenium', 'gibbet', 'laser'])
    >>> ab('fideism trophobIosis gib{be$t OGibbetP giBbet nonperjury l|ase~r evincement philoxygenous')
    True
    >>> ab = about(['incommensurable'])
    >>> ab('electroluminescence savanilla gastropleuritis telescope infectionist beetleheaded uncrude laryngograph')
    False
    >>> ab = about(['unexcusableness', 'bismuthyl', 'adapt'])
    >>> ab('undittoed bipennated ton EAdapt bismUthylo TuNexcusableness trisomy')
    False
    >>> ab = about(['intransigency', 'improperly', 'angiophorous'])
    >>> ab('haploid EangiophoroUsu firetrap tonlet SangiophOrouss imPro(Pe-rLyW Angiopho"rouss pintransigency dedimus')
    False
    >>> ab = about(['penceless', 'bromothymol', 'reticuloramose', 'pseudonymuncule'])
    >>> ab('ebromothYmOlj unliteral BromothyMolT pseudOnymuncule aerage pancratical vpe#nce$lEss pseudonyMunculE')
    True
    >>> ab = about(['beshag', 'monument', 'appressor', 'tutu', 'gentilize'])
    >>> ab('northwestward ebeshagb monUmen@>tz sbeshA+g] qtuT<u@ mo=num#enth semiresolute')
    False
    >>> ab = about(['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer', 'tootler', 'perithelium', 'monodelph'])
    >>> ab('stoccata ZpeRitheliUmP tooTlerA hcHeckroLl k&eraTonyx$isB Hmonodelphn')
    False
    >>> ab = about(['confidentiality', 'inclementness', 'plicator'])
    >>> ab('dejectory xplicatoR` CConfid(entiAlity (p{licatorm qpliCatorn hincleMenTness pliCa*to;r plicator oinclemENtness')
    True
    >>> ab = about(['sardius', 'tailings'])
    >>> ab('protect ks-ardiusI dTaIlingsr bush CsardiusA sardiusK myxemia moroseness')
    False
    >>> ab = about(['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis', 'revaporization'])
    >>> ab('sulfocyan expressionlessly rbes@cor;chx bescorch prEscapularisd r~odding- prescAPularis disawa rOddingB')
    True
    >>> ab = about(['transmundane', 'macintosh'])
    >>> ab('stransMundaneM dir athetoid prelectress transm]undanet unquarrelsome exsanguine Macinto}sho wtran&smundane')
    False
    >>> ab = about(['dualistic', 'becense', 'hyperingenuity', 'pulpalgia', 'gummose'])
    >>> ab('TgumMos#e Ygumm+?osE neuropore seconds YdualisticF tomin tgummosex')
    False
    >>> ab = about(['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically', 'teosinte'])
    >>> ab('^tenTacle pluriparous alluvial wTEoSi.n}te chrysophilite cinereal')
    True
    >>> ab = about(['clique', 'spuriae', 'introspectable', 'pyritology', 'marbleize', 'blooddrop', 'prickingly', 'ecole'])
    >>> ab('gspuriAe c*l%iQue phosphuret sPUriaen blooDdropm lclique &bloo:ddrop blooddrop')
    True
    >>> ab = about(['hiro'])
    >>> ab('untakableness borderlander hiro moviedom atmosphereless')
    True
    >>> ab = about(['disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily', 'ternarious', 'riven', 'concamerated'])
    >>> ab("lTe'rna!riousP theophagous disdiaclastic QfIbrillifeRous ternarious micrography GloomilyD")
    True
    >>> ab = about(['nonfanciful', 'aneuploidy', 'unrubified', 'dynamic', 'twistable', 'mesmerically', 'heyday', 'hipmold', 'epiprecoracoid'])
    >>> ab('thiophenic munrubi_fied lunRubifiedO circumparallelogram xUnrub/ified Ldynam&ic predelinquently')
    False
    >>> ab = about(['prorectorate', 'snappable', 'pholadoid', 'toxicodermatitis', 'gallification', 'survival', 'rakshasa', 'pungey'])
    >>> ab('silly pholadoid snappable h"s\'nappableH R,aKs-hasa nsnappabLeW snapPable Lsnappab_le')
    True
    >>> ab = about(['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear', 'writer'])
    >>> ab('Eprincip*iat_eX ;caco[mixlel writ<eRE qUadraticale Ewriter awRiterK endonucle#arN writer Zwrit|er')
    True
    >>> ab = about(['upraisal', 'mechanicalist', 'losing', 'emancipation', 'counterquarterly', 'oppress', 'dishonorable', 'liang', 'weirdly'])
    >>> ab('JmeChANicalIst bLi.an`g preambular exemplifiable SCoun^ter^quaRteRly versed')
    False
    >>> ab = about(['subframe', 'infinitude'])
    >>> ab('P@iNf{IniTude triakisoctahedrid gyroscope underdoing hinfinitude kulang Minfinitude')
    False
    >>> ab = about(['gmbh', 'isocheimal', 'overusually', 'supercargoship', 'contemptuous', 'undrawn', 'catchpollery', 'unfinishedness', 'coolie'])
    >>> ab('unfinishednessA ZGmbh stoneweed ksuper[cargoshi>pw unf*inis)hednessu')
    False
    >>> ab = about(['lazzarone', 'define'])
    >>> ab('coffeegrowing glaz:zaronev coralloidal strombite faky')
    False
    >>> ab = about(['either', 'ungenuine', 'dealable', 'pejorism', 'cointersecting', 'outerly'])
    >>> ab('twal ouTe(rl!yB ungenuinel bianisidine ipeJoRism')
    False
    >>> ab = about(['reinsertion', 'moted', 'narcoanesthesia', 'tanbur', 'sulphamidic', 'monopersulfuric', 'heartsickening', 'talkathon'])
    >>> ab('organoid Kmoted precollege dtalkathOnQ BtalKaThon')
    False
    >>> ab = about(['yond'])
    >>> ab('refrustrate altered spiderflower N~yond(c yond rectocolonic caner')
    True
    >>> ab = about(['randannite', 'overappraise', 'disdiapason', 'unclement', 'cesser', 'repatronize', 'sacerdotalist', 'atelectatic', 'plasma'])
    >>> ab('mat~ElEctatic$ unclement ksacerdot@aliSt saCerdotaliStZ repatronizes rAndanNite}m')
    True
    """
