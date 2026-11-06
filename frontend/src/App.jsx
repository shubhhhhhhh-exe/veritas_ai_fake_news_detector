import React, { useState } from 'react';

// Set this to your Render backend link once deployed (or local IP for testing)
const API_URL = 'https://YOUR-RENDER-URL.onrender.com/predict';

export default function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!text.trim()) return;
    setLoading(true);
    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setResult(data);
    } catch (err) {
      alert("Error reaching prediction server.");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: '600px', margin: 'auto' }}>
      <h1>VeritasAI Fake News Detector</h1>
      <textarea
        rows="6"
        style={{ width: '100%', padding: '10px', fontSize: '1rem' }}
        placeholder="Paste news article content here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button
        onClick={handleAnalyze}
        disabled={loading}
        style={{ marginTop: '10px', padding: '10px 20px', cursor: 'pointer' }}
      >
        {loading ? 'Analyzing...' : 'Analyze Article'}
      </button>

      {result && (
        <div style={{ marginTop: '20px', padding: '15px', border: '1px solid #ccc', borderRadius: '5px' }}>
          <h2>Result: {result.label}</h2>
          <p>Real News Probability: {result.real_probability}%</p>
          <p>Fake News Probability: {result.fake_probability}%</p>
        </div>
      )}
    </div>
  );
}
