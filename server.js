const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 5000;

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const projectName = req.body.projectName;
        const fileType = req.body.fileType;

        const baseUploadsPath = path.join(__dirname, 'uploads');
        const projectFolderPath = path.join(baseUploadsPath, projectName);

        // Create project folder if it doesn't exist
        if (!fs.existsSync(projectFolderPath)) {
            fs.mkdirSync(projectFolderPath, { recursive: true });
        }

        // Determine file type folder (img or txt)
        const fileTypeFolder = fileType === 'img' ? 'image' : 'txt';
        const fileTypeFolderPath = path.join(projectFolderPath, fileTypeFolder);

        // Create file type folder if it doesn't exist
        if (!fs.existsSync(fileTypeFolderPath)) {
            fs.mkdirSync(fileTypeFolderPath, { recursive: true });
        }

        cb(null, fileTypeFolderPath);
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname);
    }
});

const upload = multer({ storage: storage });

app.use(express.static(__dirname));

app.post('/upload', upload.array('files[]'), (req, res) => {
    res.send('Files uploaded successfully!');
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
