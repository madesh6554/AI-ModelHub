import React, { useState, useEffect } from 'react';
import './App.css';
import ModelCard from './components/ModelCard';
import ModelModal from './components/ModelModal';

const models = [
  {
    id: 1,
    name: 'StoryTeller',
    description: 'AI-powered story generator for kids with various themes',
    category: 'Gen AI',
    url: '/gen-ai/StoryTeller.html'
  },
  {
    id: 2,
    name: 'DietPlanner',
    description: 'Personalized AI diet planning assistant for various health goals',
    category: 'Gen AI',
    url: '/gen-ai/DietPlanner.html'
  },
  {
    id: 3,
    name: 'Gemini Analyzer',
    description: 'Advanced AI Model for Image and Text Analysis',
    category: 'Multimodal',
    url: 'https://gemini-analyzer.onrender.com/'
  },
  {
    id: 4,
    name: 'Sign Translator',
    description: 'Sign Language Translation (Text to Sign Language)',
    category: 'Multimodal',
    url: 'https://sign.mt/'
  },
  {
    id: 5,
    name: 'Model 5',
    description: 'Multimodal AI Model',
    category: 'Multimodal',
    url: ''
  },
  {
    id: 6,
    name: 'Model 6',
    description: 'Natural Language Processing Model',
    category: 'NLP',
    url: ''
  },
  {
    id: 7,
    name: 'Model 7',
    description: 'Computer Vision Model',
    category: 'Vision',
    url: ''
  },
  {
    id: 8,
    name: 'Model 8',
    description: 'Audio Processing Model',
    category: 'Audio',
    url: ''
  },
  {
    id: 9,
    name: 'Model 9',
    description: 'General AI Model',
    category: 'Gen AI',
    url: ''
  },
  {
    id: 10,
    name: 'Model 10',
    description: 'Multimodal AI Model',
    category: 'Multimodal',
    url: ''
  }
];

// Function to update model URLs when they become available
const updateModelUrls = (urls) => {
  models.forEach(model => {
    if (urls[model.id]) {
      model.url = urls[model.id];
    }
  });
};

// Example usage - you can call this function whenever you have new URLs
// updateModelUrls({
//   1: 'url_for_model_1',
//   2: 'url_for_model_2',
//   // ... other URLs
// });

function App() {
  const [selectedModel, setSelectedModel] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [isLoading, setIsLoading] = useState(true);
  const [cursorPosition, setCursorPosition] = useState({ x: 0, y: 0 });
  const [cursorVariant, setCursorVariant] = useState('default');
  const [showAboutModal, setShowAboutModal] = useState(false);

  useEffect(() => {
    // Simulate loading
    setTimeout(() => setIsLoading(false), 1000);

    // Custom cursor functionality
    let mouseX = 0;
    let mouseY = 0;
    let cursorX = 0;
    let cursorY = 0;
    let followerX = 0;
    let followerY = 0;

    const updateCursorPosition = (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    };

    const animateCursor = () => {
      // Faster response for main cursor
      cursorX += (mouseX - cursorX) * 0.8;
      cursorY += (mouseY - cursorY) * 0.8;
      
      // Closer follower with faster response
      followerX += (cursorX - followerX) * 0.6;
      followerY += (cursorY - followerY) * 0.6;

      setCursorPosition({
        x: cursorX,
        y: cursorY,
        followerX,
        followerY
      });

      requestAnimationFrame(animateCursor);
    };

    const handleMouseEnter = () => {
      setCursorVariant('hover');
    };

    const handleMouseLeave = () => {
      setCursorVariant('default');
    };

    window.addEventListener('mousemove', updateCursorPosition);
    document.querySelectorAll('button, a, .model-card').forEach(element => {
      element.addEventListener('mouseenter', handleMouseEnter);
      element.addEventListener('mouseleave', handleMouseLeave);
    });

    animateCursor();

    return () => {
      window.removeEventListener('mousemove', updateCursorPosition);
      document.querySelectorAll('button, a, .model-card').forEach(element => {
        element.removeEventListener('mouseenter', handleMouseEnter);
        element.removeEventListener('mouseleave', handleMouseLeave);
      });
    };
  }, []);

  const handleCardClick = (model) => {
    setSelectedModel(model);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    document.body.classList.toggle('dark-mode');
  };

  const handleAboutClick = () => {
    setShowAboutModal(true);
  };

  const handleCloseAboutModal = () => {
    setShowAboutModal(false);
  };

  const filteredModels = models.filter(model => {
    const matchesSearch = model.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         model.description.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesCategory = selectedCategory === 'all' || model.category.toLowerCase() === selectedCategory.toLowerCase();
    return matchesSearch && matchesCategory;
  });

  const categories = ['all', ...new Set(models.map(model => model.category))];

  return (
    <div className={`app ${darkMode ? 'dark-mode' : ''}`}>
      {/* Space Background */}
      <div className="space-background">
        {/* Moon Animation */}
        <div className="moon-container">
          <div className="moon"></div>
        </div>
        
        {/* Ethereal Smoke */}
        <div className="smoke"></div>
        
        {/* Star Field */}
        {[...Array(100)].map((_, i) => (
          <div
            key={i}
            className="star"
            style={{
              left: Math.random() * 100 + '%',
              top: Math.random() * 100 + '%',
              animationDuration: Math.random() * 10 + 15 + 's',
              animationDelay: Math.random() * 10 + 's'
            }}
          />
        ))}
      </div>

      <div className="cinematic-overlay" />
      <div
        className={`cursor ${cursorVariant}`}
        style={{
          position: 'fixed',
          left: `${cursorPosition.x}px`,
          top: `${cursorPosition.y}px`,
          transform: 'translate(-50%, -50%)'
        }}
      />
      <div
        className={`cursor-follower ${cursorVariant}`}
        style={{
          position: 'fixed',
          left: `${cursorPosition.followerX}px`,
          top: `${cursorPosition.followerY}px`,
          transform: 'translate(-50%, -50%)'
        }}
      />
      <nav className="navbar">
        <div className="nav-brand">
          <span className="brand-icon">🤖</span>
          <h2>AI Model Hub</h2>
        </div>
        <div className="nav-controls">
          <div className="search-bar">
            <input
              type="text"
              placeholder="Search models..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
            <span className="search-icon">🔍</span>
          </div>
          <button className="about-button" onClick={handleAboutClick}>
            About
          </button>
          <button className="theme-toggle" onClick={toggleDarkMode}>
            {darkMode ? '☀️' : '🌙'}
          </button>
        </div>
      </nav>

      <header className="app-header">
        <div className="hero-section">
          <div className="hero-content">
            <h1>AI Model Hub</h1>
            <p className="hero-subtitle">
              Discover and interact with cutting-edge AI models across various domains
            </p>
            <div className="category-filters">
              {categories.map(category => (
                <button
                  key={category}
                  className={`category-filter ${selectedCategory === category ? 'active' : ''}`}
                  onClick={() => setSelectedCategory(category)}
                >
                  {category.charAt(0).toUpperCase() + category.slice(1)}
                </button>
              ))}
            </div>
            <div className="hero-stats">
              <div className="stat-item">
                <span className="stat-number">{models.length}+</span>
                <span className="stat-label">AI Models</span>
              </div>
              <div className="stat-item">
                <span className="stat-number">{categories.length - 1}</span>
                <span className="stat-label">Categories</span>
              </div>
              <div className="stat-item">
                <span className="stat-number">100%</span>
                <span className="stat-label">Open Source</span>
              </div>
            </div>
          </div>
          <div className="hero-illustration">
            <div className="illustration-box">
              <div className="ai-brain"></div>
              <div className="ai-network"></div>
            </div>
          </div>
        </div>
      </header>

      <main>
        {isLoading ? (
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <p>Loading AI Models...</p>
          </div>
        ) : (
          <div className="model-grid">
            {filteredModels.map((model) => (
              <ModelCard 
                key={model.id} 
                model={model} 
                onClick={() => handleCardClick(model)}
              />
            ))}
          </div>
        )}
      </main>

      {showAboutModal && (
        <div className="modal-overlay" onClick={handleCloseAboutModal}>
          <div className="about-modal" onClick={e => e.stopPropagation()}>
            <button className="close-button" onClick={handleCloseAboutModal}>×</button>
            <h2>About AI Model Hub</h2>
            <div className="about-content">
              <div className="about-intro">
                <p className="main-description">
                  AI Model Hub is a comprehensive platform designed to showcase and provide access to cutting-edge AI models across various domains. Our mission is to make advanced AI technology accessible, understandable, and usable for everyone.
                </p>
                <div className="project-overview">
                  <h3>Project Overview</h3>
                  <p>
                    This platform serves as a central repository for AI models, offering:
                  </p>
                  <ul className="feature-list">
                    <li>Easy access to state-of-the-art AI models</li>
                    <li>Interactive demonstrations of model capabilities</li>
                    <li>Comprehensive documentation and usage guidelines</li>
                    <li>Real-time model performance monitoring</li>
                  </ul>
                </div>
              </div>

              <div className="about-features">
                <div className="feature-item">
                  <span className="feature-icon">🚀</span>
                  <h3>Advanced Models</h3>
                  <p>Access state-of-the-art AI models across various domains including NLP, Computer Vision, Audio Processing, and more.</p>
                </div>
                <div className="feature-item">
                  <span className="feature-icon">🔍</span>
                  <h3>Easy Discovery</h3>
                  <p>Find the perfect model for your needs with our intuitive search and category-based filtering system.</p>
                </div>
                <div className="feature-item">
                  <span className="feature-icon">🔄</span>
                  <h3>Real-time Updates</h3>
                  <p>Stay current with the latest AI model developments and improvements in real-time.</p>
                </div>
              </div>

              <div className="model-categories">
                <h3>Available Model Categories</h3>
                <div className="category-grid">
                  <div className="category-item">
                    <span className="category-icon">📝</span>
                    <h4>NLP Models</h4>
                    <p>Natural Language Processing models for text analysis and generation</p>
                  </div>
                  <div className="category-item">
                    <span className="category-icon">👁️</span>
                    <h4>Vision Models</h4>
                    <p>Computer Vision models for image and video processing</p>
                  </div>
                  <div className="category-item">
                    <span className="category-icon">🎵</span>
                    <h4>Audio Models</h4>
                    <p>Audio processing models for sound analysis and generation</p>
                  </div>
                  <div className="category-item">
                    <span className="category-icon">🤖</span>
                    <h4>Gen AI</h4>
                    <p>General AI models for versatile applications</p>
                  </div>
                  <div className="category-item">
                    <span className="category-icon">🔄</span>
                    <h4>Multimodal</h4>
                    <p>Advanced AI models that process multiple types of data simultaneously</p>
                  </div>
                </div>
              </div>

              <div className="about-stats">
                <div className="stat">
                  <span className="stat-number">{models.length}+</span>
                  <span className="stat-label">AI Models</span>
                </div>
                <div className="stat">
                  <span className="stat-number">{categories.length - 1}</span>
                  <span className="stat-label">Categories</span>
                </div>
                <div className="stat">
                  <span className="stat-number">24/7</span>
                  <span className="stat-label">Availability</span>
                </div>
              </div>

              <div className="about-footer">
                <p className="footer-text">
                  Join us in exploring the future of AI technology. Whether you're a researcher, developer, or AI enthusiast, AI Model Hub provides the tools and resources you need to leverage the power of artificial intelligence.
                </p>
              </div>
            </div>
          </div>
        </div>
      )}

      {showModal && (
        <ModelModal
          model={selectedModel}
          onClose={handleCloseModal}
        />
      )}
    </div>
  );
}

export default App;
