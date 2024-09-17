// src/BucketCreator.js
import React, { useState } from 'react';
import axios from 'axios';

const BucketCreator = () => {
    const [bucketName, setBucketName] = useState('');
    const [name, setName] = useState('');
    const [loading, setLoading] = useState(false);

    const createBucket = async () => {
        setLoading(true);
        try {
            const response = await axios.post('http://localhost:5000/createbucket', { name });
            setBucketName(response.data.bucket_name);
        } catch (error) {
            console.error("Error creating bucket:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Create S3 Bucket</h1>
            <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter Bucket Suffix"
            />
            <button onClick={createBucket} disabled={loading}>
                {loading ? 'Creating...' : 'Create Bucket'}
            </button>
            {bucketName && (
                <p>Bucket: {bucketName} created successfully!</p>
            )}
        </div>
    );
};

export default BucketCreator;
