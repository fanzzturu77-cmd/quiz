// Netlify Serverless Function: /.netlify/functions/leaderboard
// Provides cross-device cloud sync for Demokrasi Challenge on Netlify
// Uses Netlify Blobs if available in Netlify environment, with fallback to external cloud store

const CLOUD_FALLBACK_URL = 'https://api.restful-api.dev/objects/ff808181a09d98f701a17051048a01f0';

exports.handler = async function(event, context) {
    const headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
        'Content-Type': 'application/json'
    };

    if (event.httpMethod === 'OPTIONS') {
        return { statusCode: 200, headers, body: '' };
    }

    try {
        // Handle GET: retrieve current leaderboard
        if (event.httpMethod === 'GET') {
            try {
                // If Netlify Blobs is available
                const { getStore } = require('@netlify/blobs');
                const store = getStore('demokrasi-leaderboard');
                const data = await store.get('entries', { type: 'json' });
                if (data && Array.isArray(data)) {
                    return { statusCode: 200, headers, body: JSON.stringify({ entries: data }) };
                }
            } catch (err) {
                // Fallback to public REST API
            }

            const res = await fetch(CLOUD_FALLBACK_URL);
            const json = await res.json();
            const entries = json?.data?.entries || [];
            return { statusCode: 200, headers, body: JSON.stringify({ entries }) };
        }

        // Handle POST / PUT: save or update leaderboard
        if (event.httpMethod === 'POST' || event.httpMethod === 'PUT') {
            const body = JSON.parse(event.body || '{}');
            const entries = body.entries || [];

            try {
                const { getStore } = require('@netlify/blobs');
                const store = getStore('demokrasi-leaderboard');
                await store.setJSON('entries', entries);
            } catch (err) {
                // Fallback to public REST API
            }

            await fetch(CLOUD_FALLBACK_URL, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name: 'Demokrasi Leaderboard',
                    data: { entries }
                })
            });

            return {
                statusCode: 200,
                headers,
                body: JSON.stringify({ success: true, count: entries.length })
            };
        }

        return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method Not Allowed' }) };
    } catch (err) {
        return {
            statusCode: 500,
            headers,
            body: JSON.stringify({ error: err.message })
        };
    }
};
