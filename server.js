const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const app = express();
const port = 5000;

app.use(cors());
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const relativePath = path.join('uploads', path.dirname(file.originalname));
        const fullPath = path.join(__dirname, relativePath);

        if (!fs.existsSync(fullPath)){
            fs.mkdirSync(fullPath, { recursive: true });
        }

        cb(null, relativePath);
    },
    filename: (req, file, cb) => {
        cb(null, path.basename(file.originalname));
    }
});

const upload = multer({ storage: storage });

app.post('/upload', upload.array('files[]'), (req, res) => {
    res.json({message: 'Folder uploaded successfully!'});
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
