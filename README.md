# La Rosa del Deserto di Seddrak – sito vetrina

Sito del fiorista **Youssef Seddrak**, due chioschi di fiori e piante a Roma:

- **Largo Ferdinando Gregorovius** (angolo Via Macedonia), 00179 Roma – Appio Latino
- **Largo Santi Martiri dell'Uganda**, 00147 Roma – Montagnola / Laurentina

Dominio: **https://larosadeldesertodiseddrack.it**

## Come funziona

Il sito è scritto in **Python + Flask**, ma online va **solo HTML/CSS/JS statico** su GitHub Pages:
nessun server, nessun database, nessun costo di hosting, caricamento velocissimo.

```
app/
  site_data.py      ← TUTTI i dati: nome, telefono, email, IBAN, indirizzi, servizi
  data/posts.json   ← articoli del blog (migrati da WordPress)
  data/images.json  ← elenco foto ottimizzate
  templates/        ← pagine HTML (Jinja)
  static/           ← CSS, JS, logo, font, foto WebP
freeze.py           ← genera il sito statico in build/
run.py              ← anteprima locale
.github/workflows/deploy.yml  ← pubblicazione automatica a ogni push su main
```

### Modificare il sito

1. Cambia i dati in `app/site_data.py` (es. orari dei chioschi in `"hours"`, P.IVA in `"vat"`).
2. Fai commit e push su `main`: GitHub esegue i test, genera il sito e lo pubblica in ~1 minuto.

### Anteprima sul computer

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python run.py            # http://127.0.0.1:5000
python -m pytest         # test
python freeze.py         # genera build/
```

## Funzioni

| Funzione | Come |
|---|---|
| **Prenota i tuoi fiori online** (`/prenota/`) | Nome, cognome, email, telefono, indirizzo di consegna o ritiro al chiosco, calendario, fascia oraria, budget, biglietto. Arriva una **email a Youssef** e una **ricevuta al cliente** tramite [FormSubmit](https://formsubmit.co). Se l'invio fallisce, il cliente può mandare tutto su WhatsApp con un tocco. |
| **Installa la app** | Il sito è una PWA: Chrome/Android mostra "Installa", su iPhone appare la guida "Aggiungi alla schermata Home". Funziona anche offline (mostra il pulsante Chiama). |
| Contatti / preventivo | Il modulo apre WhatsApp o l'email con il messaggio già scritto. |
| Pagamenti | Bonifico (IBAN con pulsante Copia), PayPal, carta (PayPal), al chiosco. |
| SEO locale | Dati strutturati schema.org con **due attività Florist distinte** (una per chiosco), pagine dedicate per zona, sitemap, redirect dai vecchi indirizzi WordPress. |
| Omonimi | Avviso in ogni pagina: "Non abbiamo legami con ristoranti o pizzerie che si chiamano La Rosa del Deserto". |
| Google Ads | Pronto: aggiungi le variabili `GOOGLE_TAG_ID` e `GOOGLE_ADS_CALL_CONVERSION` in *Settings → Secrets and variables → Actions → Variables*. Si attivano tracciamento dei clic su Chiama/WhatsApp/Prenota e banner cookie con Consent Mode v2. |

## ⚠️ Da fare una volta

1. **Attivare FormSubmit**: alla prima prenotazione di prova arriva a `larosadeldesertoseddrak@gmail.com`
   una mail "Activate Form". Youssef deve cliccare **Activate**. Da quel momento le prenotazioni arrivano.
2. **GitHub Pages**: *Settings → Pages → Source: GitHub Actions*, poi *Custom domain*:
   `larosadeldesertodiseddrack.it` e spunta **Enforce HTTPS**.
3. **DNS del dominio** (dal pannello del registrar):
   - record `A` per `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - record `CNAME` per `www` → `carosello75.github.io`
