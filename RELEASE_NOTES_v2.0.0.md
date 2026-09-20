# KiCad AI Copilot & Auto-Router - Release Notes v2.0.0

## 🇬🇧 English
**Major Release: High-Performance Rust Engine Integration**

- **Multi-Backend Physics Engine**: Replaced standard Python routing logic with a high-performance Rust core (`rayon` multi-threading).
- **Universal Hardware Support**: Added support for Vulkan (wgpu), NVIDIA CUDA (Proprietary / Nouveau / C++), AVX2 Native CPU, and Universal CPU (`cpu_all`) backends.
- **4-Loop Vectorial A* Reroute Engine**: The system now strictly prioritizes nets (High-speed -> Analog -> RF -> Power -> GND) and utilizes an A* rip-up and retry pathfinding matrix.
- **Dynamic 1-Layer Solutions**: Automatically places `0-ohm` Jumper THT footprints for single-layer overlaps and performs real-time schematic backannotation (`.kicad_sch` text parsing).
- **4-Layer Optimization**: Automatically configures inner copper planes for VCC and GND.
- **Telemetry System**: Introduced a GDPR/KVKK-compliant opt-in telemetry system to send anonymous optimization data (routing times, rip-up counts) to the cloud for AI training improvements.
- **Compatibility**: Officially upgraded to support KiCad `10.0.6` architecture. Copyright updated to 2026.

---

## 🇹🇷 Türkçe (Turkish)
**Büyük Sürüm: Yüksek Performanslı Rust Motoru Entegrasyonu**

- **Çoklu Arka Plan Fizik Motoru**: Standart Python yönlendirme mantığı, yüksek performanslı bir Rust çekirdeği ile değiştirildi (`rayon` çoklu iş parçacığı).
- **Evrensel Donanım Desteği**: Vulkan (wgpu), NVIDIA CUDA (Kapalı Kaynak / Nouveau / C++), AVX2 CPU ve Evrensel CPU (`cpu_all`) işleme seçenekleri eklendi.
- **4-Döngülü Vektörel A* Yeniden Çizim (Rip-up) Motoru**: Sistem artık ağları kesin bir öncelik sırasına koyar (Yüksek Hız -> Analog -> RF -> Güç -> GND) ve A* tabanlı sök/yeniden dene matrisi kullanır.
- **Dinamik Tek Katman (1-Layer) Çözümleri**: Tek katmanlı PCB'lerde yolların çakışmasını önlemek için otomatik olarak `0-ohm` atlama teli ayak izlerini yerleştirir ve KiCad şematik (`.kicad_sch`) dosyasına eşzamanlı veri yazar.
- **4-Katmanlı Optimizasyon**: İç katmanları VCC ve GND bakır düzlemleri (plane) olarak otomatik tahsis eder.
- **Telemetri Sistemi**: Yapay zeka eğitimlerini iyileştirmek amacıyla, KVKK/GDPR uyumlu, kullanıcı onayı (opt-in) gerektiren anonim telemetri (yönlendirme süreleri, hata giderme sayıları vb.) sistemi eklendi.
- **Uyumluluk**: KiCad `10.0.6` mimarisi tam uyumlu hale getirildi. Telif hakları 2026 (universish) olarak güncellendi.

---

## 🇪🇸 Español (Spanish)
**Lanzamiento Principal: Integración del Motor Rust de Alto Rendimiento**

- **Motor de Física Multibackend**: Lógica de enrutamiento Python estándar reemplazada por un núcleo Rust de alto rendimiento.
- **Soporte de Hardware Universal**: Se ha añadido soporte para Vulkan (wgpu), NVIDIA CUDA, AVX2 CPU y Universal CPU (`cpu_all`).
- **Enrutamiento Vectorial A* de 4 Ciclos**: El sistema prioriza las redes estrictamente y utiliza matrices de eliminación y reintento basadas en A*.
- **Soluciones Dinámicas de 1 Capa (Single-Layer)**: Coloca automáticamente puentes `0-ohm` para colisiones de pistas en placas de 1 capa y anota retroactivamente los archivos esquemáticos (`.kicad_sch`).
- **Sistemas de Telemetría**: Se introdujo un sistema de telemetría anónimo compatible con GDPR/KVKK para mejorar el entrenamiento de IA.
- **Compatibilidad**: Oficialmente compatible con KiCad `10.0.6`.

---

## 🇳🇱 Nederlands (Dutch)
**Grote Update: Integratie van Hoogwaardige Rust-Engine**

- **Multi-Backend Fysische Engine**: De standaard Python-routeringslogica is vervangen door een krachtige Rust-kern.
- **Universele Hardware-ondersteuning**: Ondersteuning toegevoegd voor Vulkan (wgpu), NVIDIA CUDA, AVX2 CPU en Universele CPU (`cpu_all`).
- **4-Loop A* Vector Rerouting Engine**: Prioriteert signalen nauwkeurig (High-speed -> Analoog -> RF -> Power -> GND) met behulp van rip-up en retry architectuur.
- **Dynamische 1-Laag Oplossingen**: Plaatst automatisch `0-ohm` jumpers op de printplaat voor 1-laags botsingen en werkt de schema's (`.kicad_sch`) tegelijkertijd bij.
- **Telemetrie**: Een AVG/GDPR-conforme, opt-in telemetrieservice toegevoegd om anonieme routeringsgegevens te verzenden.
- **Compatibiliteit**: Bijgewerkt voor KiCad `10.0.6`.

---

## 🇨🇳 中文 (Chinese)
**主要发布：高性能 Rust 引擎集成**

- **多后端物理引擎**：使用高性能的 Rust 核心取代了标准的 Python 路由逻辑。
- **通用硬件支持**：添加了对 Vulkan (wgpu)、NVIDIA CUDA、AVX2 CPU 和通用 CPU (`cpu_all`) 的支持。
- **四次循环矢量 A* 重路由引擎**：系统现在严格确定网络优先级（高速 -> 模拟 -> 射频 -> 电源 -> GND），并使用 A* 拆除和重试寻路矩阵。
- **动态单层解决方案**：针对单层重叠问题自动放置 `0 欧姆`跳线（THT）封装，并执行实时原理图反向注释（解析 `.kicad_sch` 文本）。
- **遥测系统**：引入了符合 GDPR/KVKK 的选择性遥测系统，将匿名优化数据发送到云端。
- **兼容性**：正式升级支持 KiCad `10.0.6` 架构。版权更新为 2026 (universish)。