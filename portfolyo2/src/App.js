import React, { useState, useEffect } from 'react';

function App() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMenuActive, setIsMenuActive] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    const handleResize = () => {
      if (window.innerWidth > 768) {
        setIsMenuActive(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    window.addEventListener('resize', handleResize);
    
    // Enable smooth scrolling
    document.documentElement.style.scrollBehavior = 'smooth';
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const toggleMenu = () => {
    setIsMenuActive(!isMenuActive);
  };

  // Close menu when clicking on a nav link
  const closeMenu = () => {
    setIsMenuActive(false);
  };
  
  // Handle navigation click with smooth scrolling
  const handleNavClick = (e, targetId) => {
    e.preventDefault();
    closeMenu();
    
    const targetElement = document.getElementById(targetId);
    if (targetElement) {
      const headerOffset = 80;
      const elementPosition = targetElement.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  };

  return (
    <div className="App">
      {/* Header */}
      <header className={isScrolled ? 'scrolled' : ''}>
        <div className="container">
          <nav className="navbar">
            <a href="#home" className="logo" onClick={(e) => handleNavClick(e, 'home')}>Burak MERT</a>
            
            <ul className={`nav-menu ${isMenuActive ? 'active' : ''}`}>
              <li className="nav-item">
                <a href="#home" className="nav-link" onClick={(e) => handleNavClick(e, 'home')}>Ana sayfa</a>
              </li>
              <li className="nav-item">
                <a href="#about" className="nav-link" onClick={(e) => handleNavClick(e, 'about')}>Ben kimim?</a>
              </li>
              <li className="nav-item">
                <a href="#services" className="nav-link" onClick={(e) => handleNavClick(e, 'services')}>Neler yapabilirim?</a>
              </li>
              <li className="nav-item">
                <a href="#portfolio" className="nav-link" onClick={(e) => handleNavClick(e, 'portfolio')}>Portfolyo</a>
              </li>
              <li className="nav-item">
                <a href="#contact" className="nav-link" onClick={(e) => handleNavClick(e, 'contact')}>İletişim</a>
              </li>
            </ul>
            
            <div className={`hamburger ${isMenuActive ? 'active' : ''}`} onClick={toggleMenu}>
              <span className="bar"></span>
              <span className="bar"></span>
              <span className="bar"></span>
            </div>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hero" id="home">
        <div className="container">
          <div className="hero-content">
            <div className="hero-text">
              <h1>Merhaba</h1>
              <p>Ben bilgisayar mühendisliği 2. sınıf öğrencisiyim. Modern web uygulamaları ve yazılım dillerinde kendimi geliştirmek için çalışıyorum.</p>
              <a href="#about" className="btn" onClick={(e) => handleNavClick(e, 'about')}>DAHA FAZLA</a>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="about" id="about">
        <div className="container">
          <div className="section-title">
            <h2>Ben Kimim?</h2>
          </div>
          
          <div className="about-content">
            <div className="about-img">
              <img src="/image/profile.jpg" alt="Profile" />
            </div>
            <div className="about-text">
              <h3>Merhaba, ben bilgisayar mühendisliği öğrencisiyim.</h3>
              <p>Python, C#, HTML, Java, CSS, React gibi programlama dillerinde temel ve orta düzeyde bilgiye sahibim. PyQt5 ve Qt Designer kullanarak masaüstü uygulamaları geliştiriyorum. Ayrıca 3D modelleme konusunda Fusion 360 ile çalışmalarda bulundum.</p>
              <p>Şu ana kadar çeşitli bireysel ve ders projelerinde yer aldım. Özellikle yazılım geliştirme, kullanıcı arayüz tasarımı ve algoritma geliştirme konularına ilgi duyuyorum. Öğrenmeye ve kendimi geliştirmeye açık biriyim.</p>
              <div className="social-links">
                <a href="https://x.com/burakmaery" className="social-link" target="_blank" rel="noopener noreferrer">
                  <i className="fab fa-twitter"></i>
                </a>
                <a href="https://github.com/burakkmert" className="social-link" target="_blank" rel="noopener noreferrer">
                  <i className="fab fa-github"></i>
                </a>
                <a href="https://facebook.com" className="social-link" target="_blank" rel="noopener noreferrer">
                  <i className="fab fa-facebook-f"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="services" id="services">
        <div className="container">
          <div className="section-title">
            <h2>Neler Yapabilirim?</h2>
          </div>
          
          <div className="services-grid">
            <div className="service-item">
              <div className="service-icon">
                <i className="fab fa-python"></i>
              </div>
              <h3 className="service-title">Python Uygulama Geliştirme</h3>
              <p>Python dilini kullanarak temel düzeyde masaüstü ve konsol tabanlı uygulamalar geliştirdim. Python ile geliştirdiğim projeler sayesinde yazılım geliştirme sürecini daha iyi kavradım ve her yeni projede kendimi geliştirmeye devam ediyorum. </p>
            </div>
            
            <div className="service-item">
              <div className="service-icon">
                <i className="fas fa-desktop"></i>
              </div>
              <h3 className="service-title">PyQt5 ve Qt Designer</h3>
              <p>PyQt5 ve Qt Designer kullanarak masaüstü arayüze sahip uygulamalar geliştiriyorum. Qt Designer ile tasarladığım kullanıcı arayüzlerini PyQt5 ile birleştirerek işlevsel projeler ortaya koyuyorum. PyQt5 ve Qt Designer kullanarak soru bankası uygulaması, araç servis takip sistemi ve kelime istemci gibi projeler geliştirdim.</p>
            </div>
            
            <div className="service-item">
              <div className="service-icon">
                <i className="fas fa-database"></i>
              </div>
              <h3 className="service-title">Veritabanı Entegrasyonu</h3>
              <p>Projelerimde SQLite veritabanı kullanarak temel düzeyde veri saklama ve yönetim işlemleri gerçekleştirdim. PyQt5 ile geliştirdiğim masaüstü uygulamalarda veritabanı bağlantılarını entegre ederek kalıcı veri yönetimi sağladım. SQL sorgularını Python içerisinde kullanarak veritabanı işlemlerinin arka plan mantığını daha iyi kavradım.</p>
            </div>
            
            <div className="service-item">
              <div className="service-icon">
                <i className="fas fa-code"></i>
              </div>
              <h3 className="service-title">Web Geliştirme</h3>
              <p>HTML ve CSS kullanarak temel seviyede web sayfaları tasarlayabiliyorum.Tasarımdan kodlamaya kadar web projelerini baştan sona oluşturma deneyimi edindim. Kendi portföy sayfamı oluşturarak hem öğrendiklerimi uyguluyor hem de çalışmalarımı sergiliyorum.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Portfolio Section */}
      <section className="portfolio" id="portfolio">
        <div className="container">
          <div className="section-title">
            <h2>Portfolyo</h2>
          </div>
          
          <div className="portfolio-grid">
            <div className="portfolio-item">
              <a href="https://github.com/burakkmert/sorubankasi-pyqt" target="_blank" rel="noopener noreferrer">
                <img src="/image/sorubankasi.jpg" alt="Soru Bankası Uygulaması" className="portfolio-img" />
                <div className="portfolio-info">
                  <h3 className="portfolio-title">Soru Bankası Uygulaması</h3>
                  <p className="portfolio-category">Python ve Qt Widgets</p>
                </div>
              </a>
            </div>
            
            <div className="portfolio-item">
              <a href="https://github.com/burakkmert/servisuygulamas-" target="_blank" rel="noopener noreferrer">
                <img src="/image/servisuygulamasi.jpg" alt="Araba Servis Uygulaması" className="portfolio-img" />
                <div className="portfolio-info">
                  <h3 className="portfolio-title">Araba Servis Uygulaması</h3>
                  <p className="portfolio-category">PyQt5</p>
                </div>
              </a>
            </div>
            
            <div className="portfolio-item">
              <a href="https://github.com/burakkmert/kelimeistemci" target="_blank" rel="noopener noreferrer">
                <img src="/image/metin_islemci.jpg" alt="Metin İşlemci" className="portfolio-img" />
                <div className="portfolio-info">
                  <h3 className="portfolio-title">Metin İşlemci</h3>
                  <p className="portfolio-category">Qt Designer</p>
                </div>
              </a>
            </div>
            
            <div className="portfolio-item">
              <img src="/image/web_sitesi.jpg" alt="Web Sitesi Projesi" className="portfolio-img" />
              <div className="portfolio-info">
                <h3 className="portfolio-title">Web Sitesi Projesi</h3>
                <p className="portfolio-category">HTML, CSS, JavaScript, React</p>
              </div>
            </div>
            
            <div className="portfolio-item">
              <img src="/image/yakinda_gelecek.jpg" alt="Yakında Gelecek" className="portfolio-img" />
              <div className="portfolio-info">
                <h3 className="portfolio-title">Yakında Gelecek</h3>
                <p className="portfolio-category">-</p>
              </div>
            </div>

            
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="contact" id="contact">
        <div className="container">
          <div className="section-title">
            <h2>İletişim</h2>
          </div>
          
          <div className="contact-wrapper">
            <div className="contact-info">
              <div className="contact-item">
                <div className="contact-icon">
                  <i className="fas fa-envelope"></i>
                </div>
                <div className="contact-details">
                  <h4>Email</h4>
                  <p>burakmertt80@gmail.com</p>
                </div>
              </div>
              
              <div className="contact-item">
                <div className="contact-icon">
                  <i className="fas fa-phone"></i>
                </div>
                <div className="contact-details">
                  <h4>Telefon</h4>
                  <p>+90 0537 945 71 92</p>
                </div>
              </div>
              
              <div className="contact-item">
                <div className="contact-icon">
                  <i className="fas fa-map-marker-alt"></i>
                </div>
                <div className="contact-details">
                  <h4>Konum</h4>
                  <p>Balıkesir, Türkiye</p>
                </div>
              </div>
              
              <div className="social-links">
                <a href="https://x.com/burakmaery" className="social-link" target="_blank" rel="noopener noreferrer">
                  <i className="fab fa-twitter"></i>
                </a>
                <a href="https://github.com/burakkmert" className="social-link" target="_blank" rel="noopener noreferrer">
                  <i className="fab fa-github"></i>
                </a>
                <a href="https://facebook.com" className="social-link" target="_blank" rel="noopener noreferrer">
                  <i className="fab fa-facebook-f"></i>
                </a>
              </div>
            </div>
            
            <form className="contact-form">
              <div className="form-group">
                <input type="text" className="form-control" placeholder="Ad Soyad" required />
              </div>
              
              <div className="form-group">
                <input type="email" className="form-control" placeholder="Mail" required />
              </div>
              
              <div className="form-group">
                <textarea className="form-control" placeholder="İçerik" required></textarea>
              </div>
              
              <button type="submit" className="btn">Gönder</button>
            </form>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <div className="container">
          <p>&copy; 2025 Tüm hakları saklıdır.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
