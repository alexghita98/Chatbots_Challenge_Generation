const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();

const SECRET = 'weaksecret123'; // Hardcoded weak secret

app.get('/login', (req, res) => {
  const token = jwt.sign({ user: 'guest' }, SECRET);
  res.send(`Your token: ${token}`);
});

app.get('/flag', (req, res) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).send('Missing token');

  try {
    const decoded = jwt.verify(token, SECRET);
    if (decoded.user === 'admin') {
      return res.send(`FLAG{jwt_n0nc3_byp4ss}`);
    }
    res.status(403).send('Admin access required');
  } catch (err) {
    res.status(401).send('Invalid token');
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));