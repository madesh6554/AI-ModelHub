import React from 'react';
import './ModelModal.css';

const GEMINI_URL = 'https://gemini-analyzer.onrender.com/';

function ModelModal({ model, onClose }) {
  const handleOpenGemini = () => {
    window.open(GEMINI_URL, '_blank');
    onClose();
  };

  const getInputComponent = () => {
    if (model.category.toLowerCase() === 'multimodal') {
      return (
        <div className="gemini-section">
          <p>Click to open Gemini Analyzer in a new tab</p>
          <button className="gemini-button" onClick={handleOpenGemini}>
            Open Gemini Analyzer
          </button>
        </div>
      );
    }

    switch (model.category.toLowerCase()) {
      case 'nlp':
        return (
          <div className="input-section">
            <textarea placeholder="Enter text here..." className="text-input"></textarea>
          </div>
        );
      case 'vision':
        return (
          <div className="input-section">
            <input type="file" accept="image/*" className="file-input" />
          </div>
        );
      case 'audio':
        return (
          <div className="input-section">
            <input type="file" accept="audio/*" className="file-input" />
          </div>
        );
      default:
        return (
          <div className="input-section">
            <textarea placeholder="Enter input here..." className="text-input"></textarea>
          </div>
        );
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>{model.name}</h2>
          <button className="close-button" onClick={onClose}>×</button>
        </div>
        <div className="modal-body">
          <p className="model-description">{model.description}</p>
          {getInputComponent()}
          <div className="action-buttons">
            <button className="primary-button" onClick={onClose}>
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ModelModal;
