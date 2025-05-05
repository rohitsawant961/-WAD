const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Serve static files
app.use(express.static('public'));

// Basic route
app.get('/', (req, res) => {
  res.send('Hello !');
});

app.listen(port, () => {
  console.log(`App running at http://localhost:${port}`);
});
