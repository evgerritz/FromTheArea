import Head from 'next/head';
import styles from '../styles/Home.module.css';
//import('leaflet').then(obj => L)
import Leaflet from 'leaflet'

var map = Leaflet.map('map').setView([51.505, -0.09], 13);

Leaflet.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

Leaflet.marker([51.5, -0.09]).addTo(map)
    .bindPopup('A pretty CSS popup.<br> Easily customizable.')
    .openPopup();

export default function Home() {
    return (
        <div className={styles.container}>
          <Head>
            <title>Create Next App</title>
            <link rel="icon" href="/favicon.ico" />
          </Head>
          <main>
            <div id="map"></div>
          </main>
        </div>
    );
}

