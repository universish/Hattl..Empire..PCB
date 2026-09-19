# END USER LICENSE AGREEMENT (EULA) & TERMS OF SERVICE
# SON KULLANICI LİSANS SÖZLEŞMESİ (SKLS) VE HİZMET ŞARTLARI

---

## BÖLÜM 1: TÜRKÇE HUKUKİ METİN (TURKISH LEGAL TEXT)

**LÜTFEN BU SÖZLEŞMEYİ DİKKATLE OKUYUNUZ.**

Bu Son Kullanıcı Lisans Sözleşmesi (**"Sözleşme"** veya **"EULA"**), **Saffet Yavuz** (bundan böyle **"Lisans Veren"** veya **"Hak Sahibi"** olarak anılacaktır) ile bu Web Yazılımını, Bulut Tabanlı PCB Yönlendirme ve Optimizasyon Motorunu, API Arayüzlerini ve İlgili Ticari Hizmetleri (hep birlikte **"Web Platformu"** veya **"Hizmet"**) kullanan gerçek veya tüzel kişi (**"Kullanıcı"** veya **"Lisans Alan"**) arasında akdedilmiş bağlayıcı bir hukuki sözleşmedir.

Web Platformunu ziyaret ederek, hesap açarak, API anahtarı temin ederek veya Hizmeti kullanarak bu Sözleşmenin tüm şartlarını gayrikabili rücu kabul etmiş sayılırsınız. Şartları kabul etmiyorsanız Hizmeti kullanamazsınız.

---

### 1. FİKRİ MÜLKİYETİN KORUNMASI VE MÜLKİYET HAKKI
1.1. Web Platformunun kaynak kodları (TypeScript, React, Node.js/server.ts), derlenmiş ikili dosyaları, veri tabanı mimarisi, yapay zeka yönlendirme ve optimizasyon algoritmaları, IPC-2152 matematiksel simülatörü, RF 50Ω CPWG empedans çözümleyicisi, grafik arayüz tasarımları, ticari markaları ve teknik dokümantasyonu münhasıran **Saffet Yavuz**'un mülkiyetindedir.  
1.2. Bu Sözleşme, Kullanıcıya hiçbir şekilde Web Platformunun mülkiyetini veya kaynak kodlarını devretmez; yalnızca burada belirtilen sınırlı, devredilemez, alt lisanslanamaz, münhasır olmayan ve geri alınabilir bir kullanım izni (SaaS erişim lisansı) tanır.  
1.3. 5846 sayılı Fikir ve Sanat Eserleri Kanunu (FSEK), 6769 sayılı Sınai Mülkiyet Kanunu, Türk Ceza Kanunu ve uluslararası fikri mülkiyet anlaşmaları (Bern Sözleşmesi, WIPO, TRIPS) tahtında tüm haklar saklıdır.

---

### 2. İKİLİ LİSANSLAMA VE AÇIK KAYNAK / GPL SIZINTISINI ÖNLEME (ANTI-COPYLEFT)
2.1. **Mimari Bağımsızlık**: KiCad masaüstü programı içerisinde çalışan istemci Python scripti (`kicad_ai_copilot.py`), KiCad ekosistemiyle uyumluluk amacıyla GNU GPLv3 kapsamında sunulmaktadır.  
2.2. **Web ve Sunucu Yazılımının Ayrılığı**: Web Platformu, bulut algoritmaları ve API servisleri GPL KAPSAMINDA DEĞİLDİR. Web Platformu ticari, kapalı kaynaklı ve tescilli (proprietary) bir eserdir.  
2.3. **Ağ Protokolü Muafiyeti**: İstemci eklentisi ile Web Platformu arasındaki haberleşme bağımsız ağ protokolleri (HTTPS/REST/JSON/WebSocket) üzerinden gerçekleştirilir. GPLv3 Madde 0 ve Madde 2 uyarınca, bu tür ağ haberleşmesi sunucu yazılımını GPL'in türev eseri yapmaz. Lisans Veren, Affero GPL (AGPL) veya kaynak kod ifşa yükümlülüğü getiren hiçbir lisans hükmünü kabul etmemektedir.

---

### 3. KESİN YASAKLAR VE TİCARİ KISITLAMALAR
Kullanıcı, Web Platformu ile ilgili olarak doğrudan veya dolaylı olarak aşağıdaki fiilleri gerçekleştiremez:
1. **Tersine Mühendislik Yasağı**: Web Platformunun kodlarını, API yapılarını, derlenmiş istemci/sunucu betiklerini tersine mühendisliğe tabi tutamaz, decompile edemez, parçalayamaz veya kaynak kodunu çıkarmaya teşebbüs edemez.
2. **Ticari Yeniden Satış ve Yetkisiz Dağıtım**: Hizmeti, kullanıcı hesaplarını, API anahtarlarını, kota haklarını veya çıktı motorunu üçüncü şahıslara kiralayamaz, satamaz, alt lisanslayamaz, büro hizmeti (service bureau) veya üçüncü taraf SaaS aracı olarak pazarlayamaz.
3. **Yapay Zeka Modeli Eğitimi ve Kazıma (Model Distillation / Scraping Yasağı)**: Web Platformundan elde edilen yönlendirme verilerini, simülasyon sonuçlarını, topoloji ve tasarım matrislerini rakip bir yapay zeka, makine öğrenimi algoritması veya otomatik yönlendirici geliştirmek/eğitmek amacıyla otomatik veya manuel araçlarla toplayamaz, kazıyamaz (scraping) veya damıtamaz (distillation).
4. **Güvenlik Mekanizmalarını Atlama**: Kota sınırlamalarını, abonelik doğrulama kontrollerini, API yetkilendirme anahtarlarını veya güvenlik kalkanlarını manipüle edemez, aşamaz veya taklit edemez.

---

### 4. TİCARİ ABONELİK, KREDİ VE HİZMET BEDELLERİ
4.1. Web Platformu ücretsiz deneme, kullandıkça öde (kredi bazlı) veya süreli ticari abonelik modelleriyle sunulabilir. Lisans Veren, fiyatlandırma ve kota politikalarını dilediği zaman güncelleme hakkını saklı tutar.  
4.2. API anahtarının gizliliğinden Kullanıcı münhasıran sorumludur. Lisans Veren, yetkisiz API anahtarı kullanımı veya sözleşme ihlali tespit ettiğinde hesabı tek taraflı olarak derhal feshetme hakkına sahiptir.

---

### 5. GARANTİ REDDİ VE MÜHENDİSLİK SORUMLULUK SINIRI
5.1. Web Platformu ve sağlanan otomatik yönlendirme önerileri **"OLDUĞU GİBİ" (AS IS)** ve **"MEVCUT OLDUĞU KADAR" (AS AVAILABLE)** esasıyla sunulmaktadır.  
5.2. Otomatik yönlendirme çıktıları, PCB tasarımcısına yardımcı olmak üzere tasarlanmış mühendislik hesaplamalarıdır. Nihai fiziksel kart imalatı (fab/assembly) öncesinde tüm elektriksel, mekaniksel, termal ve yüksek frekans kurallarının KiCad veya yetkili CAD ortamında insan mühendis tarafından denetlenmesi (DRC doğrulaması) Kullanıcının kendi sorumluluğundadır.  
5.3. Lisans Veren; imalat hataları, kart basım kayıpları, devre yanmaları, bileşen hasarları, veri kaybı veya dolaylı ticari zararlardan hiçbir surette sorumlu tutulamaz.

---

### 6. FESİH VE HUKUKİ YAPTIRIMLAR
6.1. Kullanıcının bu Sözleşme hükümlerini ihlal etmesi halinde, Lisans Veren'in bildirimde bulunmaksızın lisansı iptal etme, API erişimini engelleme ve doğan maddi/manevi zararların tazmini için yasal yollara başvurma hakkı saklıdır.  
6.2. İhlal halinde Kullanıcı, elde ettiği yetkisiz kârı ve Lisans Veren'in maruz kaldığı tüm avukatlık ve yargılama giderlerini tazmin etmeyi kabul ve taahhüt eder.

---

### 7. UYGULANACAK HUKUK VE YETKİLİ MAHKEME
Bu Sözleşmenin yorumlanmasında ve uygulanmasında Türkiye Cumhuriyeti Hukuku uygulanır. Sözleşmeden doğabilecek her türlü ihtilafın çözümünde **İstanbul (Çağlayan) Mahkemeleri ve İcra Daireleri** münhasıran yetkilidir.

---

## SECTION 2: ENGLISH LEGAL TEXT

**PLEASE READ THIS AGREEMENT CAREFULLY BEFORE ACCESSING OR USING THE SERVICE.**

This End User License Agreement (**"Agreement"** or **"EULA"**) is a legally binding contract between **Saffet Yavuz** (hereinafter referred to as the **"Licensor"** or **"Copyright Holder"**) and any individual or legal entity (**"User"** or **"Licensee"**) accessing or utilizing the Web Application, Cloud Routing & Optimization Engine, API Services, and Related Commercial Software (collectively, the **"Web Platform"** or **"Service"**).

By accessing, registering an account, obtaining an API key, or using the Web Platform, you irrevocably agree to be bound by all terms and conditions of this Agreement. If you do not agree, you are prohibited from using the Service.

---

### 1. INTELLECTUAL PROPERTY & PROPRIETARY OWNERSHIP
1.1. The Web Platform's source code (TypeScript, React, Node.js/server.ts), compiled binaries, database architectures, artificial intelligence routing heuristics, IPC-2152 mathematical solvers, RF 50Ω CPWG impedance engines, graphical interfaces, trademarks, and documentation are the exclusive intellectual and proprietary property of **Saffet Yavuz**.  
1.2. This Agreement grants the Licensee a limited, non-exclusive, non-transferable, revocable, non-sublicensable right to access the Service solely for intended internal PCB engineering purposes. No ownership, source code transfer, or assignment of intellectual property is granted.  
1.3. All rights are strictly reserved under applicable national and international copyright statutes (including the Berne Convention, WIPO Copyright Treaty, and TRIPS Agreement).

---

### 2. DUAL ARCHITECTURE & ANTI-COPYLEFT CONTAMINATION (GPL EXCLUSION)
2.1. **Architectural Separation**: The client-side desktop script operating in KiCad (`kicad_ai_copilot.py`) is distributed under GNU GPLv3 for compatibility with KiCad's local ecosystem.  
2.2. **Proprietary Web Backend**: The Web Platform, cloud calculation engines, and API services ARE NOT GOVERNED BY THE GPL. The Web Platform is strictly closed-source, commercial, and proprietary.  
2.3. **Network Interaction Exemption**: Client-server communications operate solely over standard network boundaries (HTTPS/REST/JSON/WebSocket). Under Section 0 and Section 2 of GPLv3, network interactions do not constitute a derivative work. The Licensor explicitly disclaims and rejects the Affero General Public License (AGPLv3); accessing the Web Platform across a network creates no obligation whatsoever to disclose or license the server source code.

---

### 3. STRICT PROHIBITIONS & COMMERCIAL RESTRICTIONS
The Licensee shall not, directly or indirectly:
1. **Reverse Engineer**: Decompile, reverse assemble, reverse engineer, decrypt, or extract source code or underlying mathematical models from the Web Platform or its APIs.
2. **Unauthorized Reselling & Sublicensing**: Sell, sublicense, rent, lease, time-share, or distribute API keys, output engines, or access to the Service as a service bureau, white-label, or unauthorized third-party commercial platform.
3. **AI Model Training & Scraping Prohibited (Anti-Distillation)**: Scrape, harvest, or utilize routing topologies, simulation datasets, or outputs generated by the Web Platform to train, benchmark, fine-tune, or develop any competing artificial intelligence model, machine learning algorithm, or auto-router.
4. **Circumvention of Security**: Tamper with, bypass, spoof, or breach authentication tokens, billing layers, rate limits, or access credentials.

---

### 4. SUBSCRIPTIONS, QUOTAS, AND PAYMENTS
4.1. The Service may be offered via subscription tiers, pay-per-use credits, or commercial enterprise licenses. The Licensor reserves the right to modify pricing, features, and quotas at its sole discretion.  
4.2. The Licensee is solely responsible for maintaining the confidentiality of their API credentials. The Licensor reserves the right to terminate access immediately upon detection of abuse or violation of this Agreement.

---

### 5. DISCLAIMER OF WARRANTIES & LIMITATION OF LIABILITY
5.1. THE SERVICE IS PROVIDED ON AN **"AS IS"** AND **"AS AVAILABLE"** BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO MERCHANTABILITY, FITNESS FOR A PARTICULAR ELECTRICAL PURPOSE, OR FREEDOM FROM FABRICATION DEFECTS.  
5.2. Automated routing outputs are assistive engineering recommendations. The User remains solely responsible for validating all physical, thermal, RF, and electrical design rules (DRC) within KiCad or equivalent verification tools prior to physical board fabrication (PCB manufacturing/assembly).  
5.3. IN NO EVENT SHALL THE LICENSOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES, INCLUDING FABRICATION EXPENSES, DESTROYED SILICON, FIRE HAZARDS, BOARD RE-SPIN COSTS, LOST PROFITS, OR LOSS OF DATA ARISING FROM THE USE OF THE SERVICE.

---

### 6. TERMINATION & REMEDIES
6.1. The Licensor reserves the right to terminate or suspend access immediately without notice if the Licensee breaches any provision of this Agreement.  
6.2. In the event of an intellectual property breach, the Licensor shall be entitled to seek injunctive relief, statutory damages, and recovery of full legal fees to the maximum extent permitted by law.

---

### 7. GOVERNING LAW & EXCLUSIVE JURISDICTION
This Agreement shall be governed by and construed in accordance with the laws of the **Republic of Turkey**, without regard to conflict of law principles. The courts and execution offices of **Istanbul (Çağlayan), Turkey**, shall have exclusive jurisdiction over any disputes arising out of or in connection with this Agreement.
