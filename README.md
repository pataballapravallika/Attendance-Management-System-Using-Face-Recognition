
## Attendance Management System using Face Recognition


Attendance Management System Using Face Recognition is a desktop application designed to automate attendance tracking for organizations, schools, or workplaces. It uses real-time face recognition technology to detect and identify individuals, marking their attendance automatically and storing the data securely. The project is ideal for administrators seeking an efficient, accurate, and hassle-free way to manage attendance records, eliminate manual errors, and generate reports with ease.


## Demo
- The system captures a student's face using the camera.
- It compares the captured face with stored photo samples in the database.
- If a match is found, the student is marked as Present, and their attendance is saved.
- If no match is found, the system displays Unknown Face.
- The system logs attendance and saves data for recognized faces in the database.
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Gif/Gif.gif?raw=true)
- Take a stream of images from the webcam using OpenCV
- The face detection model detects where in the image faces are located. It doesn’t recognize whose face
- We feed the face to the face embedding model to get an embedding, or feature vector, of the face: a vector of size 128
- Now compare this vector to those of your buddies and find the most similar one.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*R-ObQiGjDK4Njd5tSQEz5g.png)

- Face matches
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*zCKH606XA7hdS86l0ApN8A.gif)

- Face not matches


![](https://b2633864.smushcdn.com/2633864/wp-content/uploads/2018/02/deep_learning_face_detection_opencv.gif?lossy=2&strip=1&webp=1)

## Technologies Used
- **Python:** The main programming language used to develop the application, chosen for its simplicity and extensive library support. 
- **OpenCV:** A powerful library used for real-time image processing and computer vision tasks, including face detection.
- **Face Recognition Library:** A Python library used for accurate and easy-to-implement face recognition, leveraging deep learning models for facial feature extraction and comparison.
- **Tkinter:** A standard Python library for creating graphical user interfaces (GUI), used to design the front-end interface for managing attendance records.
- **MySQL:** A relational database management system used for securely storing and managing attendance data, ensuring scalability and data integrity.
- **NumPy:** A library for numerical computing, used to handle and manipulate arrays, often involved in image processing tasks.
## Features

- Live previews
- Fullscreen mode
- Cross platform


## Screenshots
- **Main page Screenshot**
Here's a snapshot of the main page interface of the Attendance Management System.
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Screenshots/MainPage.png?raw=true)
- **Student Details Screenshot:**
In this screen, you can take a photo sample to save a student's data in the system.
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Screenshots/StudentDetails.png?raw=true)
- **Face Recognition Screenshot:**
To take attendance, click on the **Face Recognition** button. The system will detect and mark attendance based on facial recognition.
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Screenshots/FaceRecognition.png?raw=true)

"Here, the Face Recognition feature detects the face and provides the associated details."
![](https://raw.githubusercontent.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/06877a11b86da5055f5eca05ce40a1a1f23296c2/Screenshots/Face%20Recognized.png)

- **Attendance Screenshot:**
Students who are present those data appear here
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Screenshots/Attendance.png?raw=true)
- **Help:**
If you have any questions contact the email address
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Screenshots/Help.png?raw=true)

- **Train Data Screenshot:**
Click on Train Data
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Screenshots/TrainData.png?raw=true)
Then it shows data which we take sample photo from student Details as shown in below
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Screenshots/Showing%20trained%20data.png?raw=true)
- **Student Details:**
 In this we have the data of the student images

- **Developer Screenshot**
![](https://raw.githubusercontent.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/06877a11b86da5055f5eca05ce40a1a1f23296c2/Screenshots/DeveloperGUI.png)

- **Exit Screenshot**
Click on **"Yes"** if you want to close otherwise click on **"NO"**
![](https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition/blob/main/Screenshots/EXIT.png?raw=true)



## Acknowledgements
- [Open CV Documentation](https://opencv.org/)
- [Face Detection with Python Using OpenCV](https://www.datacamp.com/tutorial/face-detection-python-opencv)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [MySQL Documentation](https://dev.mysql.com/doc/)
## Support

For support, email pataballapravallika@gmail.com
## Deployment
To deploy this project, follow these steps:

### Step 1: Clone the Repository
- Clone this repository to your local machine:
```bash
git clone https://github.com/pataballapravallika/Attendance-Management-System-Using-Face-Recognition.git
```
### Step 2: Install Dependencies
- Install the required Python packages:
```bash
  pip install -r requirements.txt
```

### Step 3: Set Up the MySQL Database
- Create a MySQL database named students:
sql
```sql
  CREATE DATABASE students;
```  
- Create a table attendance in the students database

``` sql
CREATE TABLE students (
    Student_id VARCHAR(45) PRIMARY KEY,
    Name VARCHAR(45),
    Division VARCHAR(45),
    Roll VARCHAR(45),
    Gender VARCHAR(45),
    Dob VARCHAR(45),
    Email VARCHAR(45),
    Phone VARCHAR(45),
    Address VARCHAR(45),
    Teacher VARCHAR(45),
    PhotoSample VARCHAR(45)
); 
```
### Step 4: Run the Application
- Run the Python application
```bash
  python main.py
```
- The Tkinter window will open for marking attendance using face recognition.
``` vbnet
In summary:
- Remove the `npm run deploy` command because it’s not applicable to a Python project.
- Use the correct Python-specific commands to install dependencies and run the application.

Let me know if you need further clarification!
```






