[09:53] Motto Lorenzo
### UniSkaven UniApp
##### ITS ICT - Gruppo di Lavoro 2

**VERSION : 0.1**

**Authors**  
Cattozzo Giacomo

**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
| 0.1 | 29/09/2022 | Giacomo| Applicazione gestionale di conti correnti per ePortafoglio |



# Table of Contents

1. [Introduction](#p1)
    1. [Document Scope](#sp1.1)
    2. [Definitios and Acronym](#sp1.2) 
    3. [References](#sp1.3)
2. [System Description](#p2)
    1. [Context and Motivation](#sp2.1)
    2. [Project Objectives](#sp2.2)
3. [Requirement](#p3)
     1. [Stakeholders](#sp3.1)
     2. [Functional Requirements](#sp3.2)
     3. [Non-Functional Requirements](#sp3.3)
    

<a name="p1"></a>

## 1. Introduction
Applicazione per gestione di conti bancari e e trasferimento di denaro, è possibile inoltre visualizzare uno storico per un certo periodo di tempo

<a name="sp1.1"></a>

### 1.1 Document Scope
Questa applicazione da la possibilità ai clienti di collegarsi tramite l'utilizzo di un username e password di gestire i conti correnti; in più si possono effettuare operazioni di trasferimento di denaro sia a conti della stessa azienda sia a conti di aziende diverse tramite codici univoci propri di ogni conto.
Inoltre si potrà anche visualizzare tutte le operazioni effettuate in un determinato perido di tempo.


<a name="sp1.2"></a>

### 1.2 Definitios and Acronym


| Acronym                | Definition | 
| ------------------------------------- | ----------- | 
|CB                      | Conto bancario |
|Trasf.                  | Trasferimento |
|EC                      | Estratto conto|


<a name="sp1.3"></a>

### 1.3 References 
ePortafoglio : proprietaria dell'applicazione
Giacomo cattozzo : Creatore applicazione

<a name="p2"></a>

## 2. System Description
Il sistema dopo aver verificato che username e password coincidano fa entrare all'interno del conto richiesto, se si vuole trasferire denaro è possibile farlo sia per conti della stessa azienda che altri tramite propri codici univoci, basterà quindi inserire il codice univoco del conto a cui si vuole trasferire il denaro e l'importo voluto.
Tramite tasto "vedi storico" potrai visualizzare tutte le operazini effettuate per un arco di tempo.

<a name="sp2.15"></a>

### 2.1 Context and Motivation


<a name="sp2.2"></a>

### 2.2 Project Obectives 
Quest'applicazione serve a raccogliere tutti i conti dei clienti dell'azienda e semplificare le transazioni sia per i clienti che per l'azienda.


<a name="p3"></a>

## 3. Requirements

| Priorità | Significato | 
| --------------- | ----------- | 
| M | **Mandatory:**   |
| D | **Desiderable:** |
| O | **Optional:**    |
| E | **future Enhancement:** |

<a name="sp3.1"></a>
### 3.1 Stakeholde

#### Utenti
| Gruppo | Ruoli | Obiettivo |
| ----------- | ----------- | ----------- |
|Direttore dell'azienda|Può modificare certi aspetti che ne i clienti ne i funzionari possono modificare | Funzionario dell'azienda|Può modificare certi aspetti sul conto del cliente con sua richiesta, può creare account ed eseguire le transazioni| Aiutare il cliente| Cliente | Destinatario finale dell'applicazione | 
#### Regolatori
| Gruppo | Ruoli |
| ----------- | ----------- | 
| Professore |  |Supporto |

#### Clienti
| Nome | Descrizione |
| ----------- | ----------- | 
|      |             |

<a name="sp3.2"></a>
### 3.2 Functional Requirements 

#### 3.2.0 Requisiti Generali
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 0.1.0 | Ogni cliente dovrà creare un suo username e password |M|
| 0.1.1 | Ogni cliente dovrà inserire la propria email |M|
| 0.1.2 | Il sistema crea gli utenti dei clienti e assegna un codice univoco |M|
| 0.1.3 | Il sistema permette di eseguire transazioni sia all'interno della stessa azienda che all'esterno |M|
| 0.1.4 | Il sistema permette di visualizzare uno storico |M|
| 0.1.5 | L'applicazione permetterà in futuro di salvare il codice univoco a cui si ha già fatto una transazione in modo da non doverlo riscrivere ogni volta |E|

#### 3.2.1 Requisiti Funzionali A


| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.1.0 |  L'amministrazione crea profili docenti |M| 
| 1.1.1 |  L'amministrazione può modificare l'ID dei docenti |M|
| 1.1.2 |  L'amministrazione può modificare i dati anagrafici dei docenti |M| 
| 1.2.0 |  L'amministrazione crea profili studenti |M|
| 1.2.1 |  L'amministrazione può modificare l'ID degli studenti |M|
| 1.3.0 |  L'amministrazione crea corsi per ogni percorso di laurea |M|
| 1.4.0 |  L'amministrazione assegna i docenti ai corsi |M|

<a name="sp3.3"></a>
### 3.3 Non-Functional Requirements 
 
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| R1 | L'applicazione deve essere compatibile con Windows, MACOS, e Linux |M|
| R2 | L'applicazione deve essere compatibile con IOS E Android|M|
| R3 | L'applicazione deve essere accessibile tramite tutti i browser |M|
| R4 | L'applicazione deve rispettare i dettami del GDPR nell'acquisizione e protezione dei dati |M|
| R5 | L'applicazionedeve appoggiarsi su un database dedicato |M|
| R6 | Il database deve avere back-up giornalieri sia in fisico che in cloud |M|
| R7 | L'applicazione deve essere disponibile anche in Inglese |M|
| R8 | L'applicazione deve essere disponibile anche in Francese |D|
| R9 | L'applicazione deve essere disponibile anche in Cinese |O|


