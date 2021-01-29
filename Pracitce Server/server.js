const express = require('express');
const fetch = require('node-fetch');

const app = express();

const port = process.env.PORT || 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(express.static('public'));



function processDataForFrontEnd(req, res) {
  const baseURL = 'https://data.princegeorgescountymd.gov/resource/wb4e-w4nf.json'; // Enter the URL for the data you would like to retrieve here

    fetch(baseURL)
      .then((r) => r.json())
      .then((data) => {
        return data
      })

      .then((data) => {
        console.log("lol", data);
        const refined = data.map((m) => ({
          CrimeType: m.clearance_code_inc_type,
          Latitude: m.latitude,
          Longitude: m.longitude,
          Date: m.date,
          Sector: m.pgpd_sector
        }));
         
          return refined
        })

        .then((data) => {
          console.log("hehe", data)
          return data.reduce((c, current) => {
            if (!c[current.CrimeType]) {

              c[current.CrimeType] = [];
            }
            c[current.CrimeType].push(current);
            return c;
          }, {});
        })

        .then((data) => {
          console.log(data);
          res.send({ data: data }); 
        })
        .catch((err) => {
          console.log(err);
          res.redirect('/error');
        });















}

// This is our first route on our server.
// To access it, we can use a "GET" request on the front end
// by typing in: localhost:3000/api or 127.0.0.1:3000/api
app.get('/api', (req, res) => {processDataForFrontEnd(req, res)});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
