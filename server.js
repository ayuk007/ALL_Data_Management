const express = require("express");
const multer = require("multer");
const cors = require("cors");
const fs = require("fs");

var app = express();
app.use(cors()); // Allows incoming requests from any IP
app.use(express.urlencoded({ extended: false }));

// Start by creating some disk storage options:
const storage = multer.diskStorage({
destination: function (req, file, callback) {
    const projectName = req.body.projectName;
    const fileType = req.body.fileType;
    const uploadPath = `${__dirname}/uploads/${projectName}`;
    const imagePath = uploadPath + "/image";
    const labelPath = uploadPath + "/label";

    // Check if the "uploads" folder exists, if not, create it
    if (!fs.existsSync(uploadPath)) {
      fs.mkdirSync(uploadPath);
      fs.mkdirSync(imagePath);
      fs.mkdirSync(labelPath);
    }
    if(fileType === "img") {
      callback(null, imagePath);
    } else {
      callback(null, labelPath);
    }
    console.log(req.body, "hleoe");
    // callback(null, uploadPath);
  },
  // Sets file(s) to be saved in uploads folder in same directory
  filename: function (req, file, callback) {
    callback(null, file.originalname);
  },
  // Sets saved filename(s) to be original filename(s)
});

// Set saved storage options:
const upload = multer({ storage: storage });

app.post("/upload", upload.array("files"), (req, res) => {
  // Sets multer to intercept files named "files" on uploaded form data

  console.log(req.body.projectName); // Logs form body values
  console.log(req.files); // Logs any files
  res.json({ message: "File(s) uploaded successfully" });
  

});

app.listen(5000, function () {
  console.log("Server running on port 5000");
});
