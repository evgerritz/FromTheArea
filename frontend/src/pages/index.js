import Head from 'next/head';

import Layout from '@components/Layout';
import Section from '@components/Section';
import Container from '@components/Container';
import Map from '@components/Map';
import Button from '@components/Button';

import { useEffect, useState } from 'react'

import styles from '@styles/Home.module.scss';

const DEFAULT_CENTER = [41.316307, -72.922585]

export default function Home() {
    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('/hello/')
            .then(res => res.json())
            .then(data => {
                setMessage(data.message);
                setLoading(false);
            })
    }, [])


    return (
        <Layout>
            <Head>
                <title>FromTheArea</title>
                <meta name="description" content="..." />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <p> {!loading ? message : "Loading.."}</p>
            <Section>
                <Container>
                    <Map className={styles.homeMap} width="3" height="2"
                        center={DEFAULT_CENTER} zoom={12}>
                    {({ TileLayer, Marker, Popup }) => (
                        <>
                        <TileLayer
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
                        />
                        <Marker position={DEFAULT_CENTER}>
                            <Popup>
                                A pretty CSS3 popup. <br /> Easily customizable.
                            </Popup>
                        </Marker>
                        </>
                    )}
                    </Map>
                </Container>
            </Section>
        </Layout>
    )
}
