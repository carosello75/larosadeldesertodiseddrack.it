"""Dati dell'attività: modifica qui nome, telefoni, indirizzi, orari e servizi.

Tutto il sito (pagine, schema.org per Google, footer, sitemap) legge da questo file,
così nome/indirizzo/telefono restano IDENTICI ovunque: è la base della SEO locale
e del profilo Google Business.
"""

BUSINESS = {
    "name": "Piante e Fiori Roma di Seddrak",
    "short_name": "Fiori Seddrak",
    "tagline": "Fiori e piante a Roma",
    "owner": "Youssef Seddrak",
    "phone": "+393899962511",          # formato internazionale per i link tel:
    "phone_display": "389 996 2511",
    "whatsapp": "393899962511",
    # Indirizzo verificato nel database del vecchio sito (82 occorrenze, "seddrak" senza la c).
    "email": "larosadeldesertoseddrak@gmail.com",
    # Le prenotazioni dal sito arrivano qui tramite FormSubmit (servizio gratuito, nessun server).
    # Alla PRIMA prenotazione FormSubmit manda a questo indirizzo una mail di attivazione:
    # Youssef deve cliccare "Activate Form" una volta sola.
    "booking_email": "larosadeldesertoseddrak@gmail.com",
    # Bonifico bancario: compila IBAN e intestatario e la sezione appare da sola
    # nella pagina Prenota (dopo l'invio) e in Pagamento online.
    "iban": "IT71 Z360 8105 1382 6862 4968 630",   # verificato (controllo mod 97)
    "iban_holder": "Seddrak Youssef Ghali Bassta",
    "bank_name": "Postepay S.p.A.",
    "paypal_url": "https://paypal.me/larosadeldeserto",
    "paypal_hosted_button_id": "76SMRDR9BKQWU",
    "paypal_client_id": "BAAPEBcaQi82YaRMhulgfxE_89qZ-N_GihtTCFIxw_ZjoksiWKvKjo-OyFdGEwFdoeSNEeDfb7sQOWao5A",
    # Obbligatoria per legge sui siti di attività italiane: inseriscila quando disponibile.
    "vat": "",
    # Link ai profili ufficiali (Google Business, Instagram, Facebook): aiutano Google a
    # distinguere QUESTA attività dagli omonimi. Aggiungili appena creati.
    "same_as": [],
    "disambiguation": (
        "Siamo un fiorista di Roma. Non abbiamo legami con ristoranti, bar, pizzerie, "
        "kebab, centri estetici o altre attività che si chiamano «La Rosa del Deserto»."
    ),
}

# Un elemento per chiosco. "hours": lista di (giorni schema.org, apertura, chiusura);
# lasciala vuota finché gli orari non sono confermati (non pubblichiamo orari inventati).
LOCATIONS = [
    {
        "slug": "gregorovius",
        "path": "fioraio-largo-ferdinando-gregorovius",
        "seo_title": "Fioraio Largo Gregorovius, Appio Latino | Fiori Seddrak",
        "seo_description": "Chiosco di fiori e piante a Largo Ferdinando Gregorovius, angolo Via Macedonia (00179 Roma). Bouquet e consegne. Tel. 389 996 2511.",
        "name": "Chiosco di Largo Ferdinando Gregorovius",
        "full_name": "Piante e Fiori Roma di Seddrak – Largo Gregorovius",
        "street": "Largo Ferdinando Gregorovius",
        "street_note": "angolo Via Macedonia",
        "postal_code": "00179",
        "city": "Roma",
        "region": "RM",
        "zone": "Appio Latino",
        "nearby": ["Via Macedonia", "Appio Latino", "Tuscolano", "Re di Roma", "Furio Camillo"],
        "lat": 41.87207,
        "lng": 12.51047,
        "phone": "+393899962511",
        "phone_display": "389 996 2511",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Largo+Ferdinando+Gregorovius+00179+Roma",
        "embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.897885605641!2d12.510475781415868!3d41.87207025554259!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x132f61e42135a205%3A0xc241d16216798484!2sLargo%20Ferdinando%20Gregorovius%2C%2000179%20Roma%20RM!5e0!3m2!1sit!2sit!4v1731091304814!5m2!1sit!2sit",
        "photo": "youssef-seddrak-cuore-di-rose",
        "hours": [],
    },
    {
        "slug": "uganda",
        "path": "fioraio-largo-santi-martiri-uganda",
        "seo_title": "Fioraio Largo S. Martiri dell'Uganda, Montagnola | Seddrak",
        "seo_description": "Chiosco di fiori e piante a Largo Santi Martiri dell'Uganda (00147 Roma), zona Montagnola e Laurentina. Tel. 389 996 2511.",
        "name": "Chiosco di Largo Santi Martiri dell'Uganda",
        "full_name": "Piante e Fiori Roma di Seddrak – Largo Santi Martiri dell'Uganda",
        "street": "Largo Santi Martiri dell'Uganda",
        "street_note": "",
        "postal_code": "00147",
        "city": "Roma",
        "region": "RM",
        "zone": "Montagnola – Laurentina",
        "nearby": ["Montagnola", "Laurentina", "EUR", "Ardeatino", "Garbatella"],
        "lat": 41.84570,
        "lng": 12.48768,
        "phone": "+393899962511",
        "phone_display": "389 996 2511",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Largo+Santi+Martiri+dell%27Uganda+00147+Roma",
        "embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2972.191486129678!2d12.487686576088018!3d41.84570506744184!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x13258a5c2e3d94d1%3A0x1ada337b451c311c!2sLargo%20Santi%20Martiri%20dell%27Uganda%2C%2000147%20Roma%20RM!5e0!3m2!1sit!2sit!4v1731091455264!5m2!1sit!2sit",
        "photo": "chiosco-fiori-roma",
        "hours": [],
    },
]

SERVICES = [
    {
        "slug": "bouquet-da-sposa",
        "seo_title": "Bouquet da sposa a Roma | Fiorista Seddrak",
        "seo_description": "Bouquet da sposa con rose, calle e peonie fatti a mano a Roma. Bouquet per damigelle e boutonnière. Preventivo gratuito: 389 996 2511.",
        "title": "Bouquet da sposa",
        "lead": "Il bouquet nasce da un incontro: ci racconti abito, colori e stagione, noi scegliamo i fiori.",
        "cat": "sposa",
        "cover": "bouquet-sposa-calle",
        "body": [
            "Rose avorio, calle, peonie, gypsophila: lavoriamo con fiori freschi scelti al mercato per il tuo giorno.",
            "Prepariamo anche bouquet per le damigelle, boutonnière per lo sposo e i testimoni, e il bouquet da lanciare.",
            "Ti consigliamo di contattarci almeno un mese prima: portaci una foto dell'abito o un'idea e ti facciamo un preventivo.",
        ],
        "quote_label": "Bouquet da sposa",
    },
    {
        "slug": "addobbi-matrimoni",
        "seo_title": "Addobbi matrimoni a Roma | Chiesa e ricevimento",
        "seo_description": "Addobbi floreali per matrimoni, battesimi e comunioni a Roma: chiesa, comune e ricevimento. Preventivo gratuito dal fiorista Seddrak.",
        "title": "Addobbi per matrimoni e cerimonie",
        "lead": "Chiesa, comune, ricevimento: allestiamo i fiori per tutta la giornata.",
        "cat": "matrimoni",
        "cover": "addobbo-floreale-chiesa",
        "body": [
            "Addobbiamo altare, navata e ingresso della chiesa, il tavolo degli sposi in comune, centrotavola e archi per il ricevimento.",
            "Seguiamo anche battesimi, comunioni, cresime e anniversari.",
            "Facciamo un sopralluogo quando serve e concordiamo insieme fiori, colori e budget.",
        ],
        "quote_label": "Addobbi matrimoniali",
    },
    {
        "slug": "fiori-per-funerali",
        "seo_title": "Fiori per funerali a Roma | Corone e cuscini",
        "seo_description": "Corone, cuscini e composizioni di cordoglio a Roma, anche urgenti. Consegna in chiesa e camera mortuaria. Chiama il 389 996 2511.",
        "title": "Fiori per funerali e cordoglio",
        "lead": "Corone, cuscini e composizioni di cordoglio, preparati con cura anche con poco preavviso.",
        "cat": "funerali",
        "cover": "corona-funebre-rose-rosse",
        "body": [
            "Realizziamo corone su cavalletto, cuscini, cuori e composizioni con nastro e dedica personalizzata.",
            "Consegniamo in chiesa, alla camera mortuaria o al cimitero nelle zone di Roma Sud.",
            "Per un ordine urgente chiamaci: ti diciamo subito i tempi di consegna.",
        ],
        "quote_label": "Fiori per funerali",
    },
    {
        "slug": "corone-di-laurea",
        "seo_title": "Corona di alloro per laurea a Roma | Fiori Seddrak",
        "seo_description": "Corone di alloro fresco per la laurea a Roma, con nastro rosso e fiori. Prenota con qualche giorno di anticipo: 389 996 2511.",
        "title": "Corone di alloro per la laurea",
        "lead": "Alloro fresco intrecciato a mano, con nastro rosso e fiori se li desideri.",
        "cat": "laurea",
        "cover": "corona-alloro-laurea",
        "body": [
            "La corona di alloro si prepara il giorno stesso o la sera prima, perché arrivi fresca alla proclamazione.",
            "Possiamo aggiungere fiori, nastri con il nome e un piccolo bouquet da regalare.",
            "Prenotala con qualche giorno di anticipo, soprattutto nei periodi di sessione.",
        ],
        "quote_label": "Corona di laurea",
    },
    {
        "slug": "bouquet-e-composizioni",
        "seo_title": "Bouquet e composizioni di fiori a Roma | Seddrak",
        "seo_description": "Mazzi di fiori e composizioni per compleanni, anniversari e regali, preparati al momento a Roma Sud. Consegna a domicilio.",
        "title": "Bouquet e composizioni",
        "lead": "Mazzi per compleanni, anniversari e per dire grazie, composti al momento.",
        "cat": "bouquet",
        "cover": "bouquet-rose-arancio-statice",
        "body": [
            "Rose, gerbere, girasoli, tulipani, lisianthus: componiamo il mazzo con i fiori di stagione più belli della giornata.",
            "Composizioni in cesto, in cappelliera o in vaso, già pronte da regalare.",
            "Dicci il budget e l'occasione: al resto pensiamo noi.",
        ],
        "quote_label": "Bouquet o composizione",
    },
    {
        "slug": "piante-terrazze-e-giardini",
        "seo_title": "Piante per casa e terrazzo a Roma | Fiori Seddrak",
        "seo_description": "Orchidee, piante verdi e fiorite, piante per terrazzi e balconi a Roma Sud, con i consigli per curarle. Consegna a domicilio.",
        "title": "Piante, terrazze e giardini",
        "lead": "Piante da interno e da esterno, e consigli per farle stare bene.",
        "cat": "piante",
        "cover": "orchidea-phalaenopsis",
        "body": [
            "Orchidee, piante grasse, piante verdi da appartamento e piante fiorite di stagione.",
            "Per terrazzi e balconi ti aiutiamo a scegliere piante adatte all'esposizione e al tempo che puoi dedicare alla cura.",
            "Ogni pianta esce dal chiosco con le indicazioni su luce, acqua e rinvaso.",
        ],
        "quote_label": "Terrazze e giardini",
    },
    {
        "slug": "natale",
        "seo_title": "Composizioni di Natale a Roma | Fiorista Seddrak",
        "seo_description": "Stelle di Natale, centrotavola con candele e mele, corone d'abete e regali aziendali a Roma Sud. Ordina per telefono o WhatsApp.",
        "title": "Natale",
        "lead": "Stelle di Natale, centrotavola con mele e candele, abeti decorati.",
        "cat": "natale",
        "cover": "composizione-natale-agrumi",
        "body": [
            "A dicembre i chioschi si riempiono di stelle di Natale rosse e bianche, ciclamini e abeti.",
            "Prepariamo centrotavola con candele, mele, agrumi e pigne, coroncine per la porta e composizioni da regalare.",
            "Per regali aziendali e ordini di più pezzi contattaci in anticipo.",
        ],
        "quote_label": "Composizioni di Natale",
    },
    {
        "slug": "san-valentino",
        "seo_title": "Fiori per San Valentino a Roma | Cuori di rose",
        "seo_description": "Cuori di rose in scatola, rose rosse e blu, cesti con cioccolatini per San Valentino a Roma. Consegna a domicilio con biglietto.",
        "title": "San Valentino e anniversari",
        "lead": "Cuori di rose, scatole con cioccolatini, rose blu e rosse.",
        "cat": "sanvalentino",
        "cover": "cuore-di-rose-in-scatola",
        "body": [
            "Cuori di rose rosse in scatola, orsetti di rose, cesti con peluche e cioccolatini.",
            "Per il 14 febbraio prenota qualche giorno prima: le richieste sono tante.",
            "Possiamo consegnare a domicilio con un biglietto scritto da te.",
        ],
        "quote_label": "San Valentino",
    },
    {
        "slug": "bouquet-di-dolci-e-regali",
        "seo_title": "Bouquet di dolci e cesti regalo a Roma | Fiori Seddrak",
        "seo_description": "Bouquet di snack e cioccolatini, cesti con peluche, orsetti di rose e palloncini a Roma Sud. Per compleanni, lauree e San Valentino. Consegna a domicilio.",
        "title": "Bouquet di dolci e regali",
        "lead": "Bouquet di snack e cioccolatini, cesti con peluche, orsetti di rose e palloncini.",
        "cat": "regali",
        "cover": "cesto-peluche-rose-e-cioccolato",
        "extra": ["youssef-seddrak-bouquet-di-snack", "youssef-seddrak-bouquet-dolci", "orsetto-di-rose-i-love-you", "scatola-cuore-rose-rosse-e-ferrero"],
        "body": [
            "Youssef prepara bouquet di dolci e snack incartati come un mazzo di fiori: un regalo diverso per compleanni, lauree e feste.",
            "Cesti e borsette con peluche, cioccolatini, una rosa e il palloncino a cuore. Anche colonne di palloncini per addobbare.",
            "Dicci per chi è e quanto vuoi spendere: lo componiamo su misura e lo consegniamo a domicilio con un biglietto.",
        ],
        "quote_label": "Bouquet di dolci e regali",
    },
    {
        "slug": "consegna-a-domicilio",
        "seo_title": "Fiori a domicilio a Roma Sud | Fiorista Seddrak",
        "seo_description": "Consegna di fiori e piante a domicilio a Appio Latino, Tuscolano, Montagnola, EUR e Garbatella. Ordina al 389 996 2511.",
        "title": "Consegna a domicilio a Roma",
        "lead": "Portiamo fiori e piante a casa, in ufficio, in chiesa o in ospedale.",
        "cat": "bouquet",
        "cover": "cesto-fiori-misti",
        "body": [
            "Consegniamo dai nostri due chioschi in Roma Sud: Appio Latino, Tuscolano, Montagnola, Laurentina, EUR, Garbatella e dintorni.",
            "Ordina per telefono o WhatsApp, scegli i fiori e paga anche online con PayPal o carta.",
            "Aggiungiamo un biglietto con il tuo messaggio.",
        ],
        "quote_label": "Consegna a domicilio",
    },
]

NAV = [
    ("Prenota", "main.booking"),
    ("Servizi", "main.services"),
    ("Galleria", "main.gallery"),
    ("Dove siamo", "main.where"),
    ("Blog", "main.blog"),
    ("Contatti", "main.contacts"),
]
