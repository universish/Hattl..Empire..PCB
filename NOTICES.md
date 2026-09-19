# THIRD-PARTY SOFTWARE NOTICES & ACKNOWLEDGMENTS
# ÜÇÜNCÜ TARAF YAZILIM BİLDİRİMLERİ VE ATIFLAR

---

## BÖLÜM 1: TÜRKÇE (TURKISH)

Bu belge, **KiCad AI PCB Copilot & Auto-Router** istemci eklentisi ve ilgili sistem bileşenleri tarafından başvurulan, entegre edilen veya birlikte çalışılan üçüncü taraf kütüphanelerin, açık kaynak yazılımların ve endüstri standartlarının lisans ve telif hakkı bildirimlerini içerir.

### 1. KiCad EDA & pcbnew Python API
- **Proje:** KiCad EDA Suite (https://kicad.org)
- **Telif Hakkı:** KiCad Developers and Contributors
- **Lisans:** GNU General Public License version 3 (GPLv3) or later
- **Açıklama:** Bu eklenti, kullanıcının yerel KiCad kurulumundaki `pcbnew` Python API arayüzünü kullanarak PCB kartı geometrisini, yollarını, via ve net tanımlarını düzenler. İstemci eklenti kodları GPLv3 şartlarıyla uyumlu olarak sunulmaktadır.

### 2. IPC Standartları ve Mühendislik Referansları
- **IPC-2152:** Standard for Determining Current-Carrying Capacity in Printed Board Design (Baskılı Devre Kartlarında Akım Taşıma Kapasitesi Standardı).
- **IPC-2221A:** Generic Standard on Printed Board Design.
- **Açıklama:** Güç hatlarının iz genişliği ve bakır kalınlığı hesaplamaları kamuya açık IPC-2152 termal denklemleri ($I = k \cdot \Delta T^{0.44} \cdot A^{0.725}$) model alınarak gerçekleştirilmektedir.

### 3. RF Mikrodalga & CPWG Empedans Formülasyonları
- **Referans:** Conductor-Backed Coplanar Waveguide (Grounded CPWG) ve Quasi-TEM Mikroşerit analitik formülleri (W.J. Getsinger, E. Hammerstad & O. Jensen).
- **Açıklama:** RF 50Ω hat genişliği ($W$) ve yer düzlemi kleransı ($S$) hesaplamaları klasik mikrodalga iletim hattı analitik denklemlerine dayanmaktadır.

---

## SECTION 2: ENGLISH

This document contains third-party software notices, open-source attributions, and engineering standard citations applicable to the **KiCad AI PCB Copilot & Auto-Router** client plugin and interoperable components.

### 1. KiCad EDA & pcbnew Python API
- **Project:** KiCad EDA Suite (https://kicad.org)
- **Copyright:** KiCad Developers and Contributors
- **License:** GNU General Public License version 3 (GPLv3) or later
- **Statement:** The desktop client plugin interfaces with the native `pcbnew` Python API provided by KiCad. The client-side plugin code is distributed in compliance with GPLv3.

### 2. IPC Standards & Engineering Formulations
- **IPC-2152:** Standard for Determining Current-Carrying Capacity in Printed Board Design.
- **IPC-2221A:** Generic Standard on Printed Board Design.
- **Statement:** High-current power trace sizing and copper thermal limits implement empirical formulations published under IPC-2152 standard guidelines.

### 3. RF / Microwave CPWG Transmission Line Formulations
- **Reference:** Conductor-Backed Coplanar Waveguide (CBCPW / Grounded CPWG) conformal mapping and analytical Quasi-TEM models.
- **Statement:** 50 Ohm RF trace width ($W$) and coplanar ground spacing ($S$) calculations are derived from established electromagnetic transmission line theory.
