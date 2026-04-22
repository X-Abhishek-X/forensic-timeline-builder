# CST4552 Coursework 2 - Submission Checklist

## 📦 Submission Package Contents

### Part 1: Report + Code (Zip File)

#### ✅ Required Documents

- [ ] **Technical Report** (`COURSEWORK_REPORT.md` or PDF version)
  - Introduction ✓
  - Problem Definition ✓
  - Flow Diagram ✓
  - Major Code Snippets ✓
  - Working/Implementation Details ✓
  - Testing & Results ✓
  - Conclusion ✓
  - Future Scope/Improvements ✓
  - References ✓

#### ✅ Code Files

- [ ] `run_all.py` - Main execution script
- [ ] `requirements.txt` - Dependencies
- [ ] `collector/collect_logs.py` - Log collection module
- [ ] `collector/ssh_hosts.json.example` - Configuration template
- [ ] `processor/normalize.py` - Normalization engine
- [ ] `processor/timeline_builder.py` - Export functions
- [ ] `processor/parsers/syslog_parser.py` - Syslog parser
- [ ] `processor/parsers/authlog_parser.py` - Auth.log parser
- [ ] `processor/parsers/windows_evtx_parser.py` - EVTX parser
- [ ] `webui/app.py` - Web interface
- [ ] All supporting files

#### ✅ Documentation

- [ ] `README.md` - User guide
- [ ] `DOCUMENTATION.md` - Technical documentation
- [ ] `BEGINNER_GUIDE.md` - Tutorial guide
- [ ] `.gitignore` - Git configuration

### Part 2: PowerPoint Presentation

#### ✅ Required Slides

- [ ] Introduction
- [ ] Problem Definition
- [ ] Flow Diagram
- [ ] Major Code Snippets (3 slides)
- [ ] Working Demo (screenshots/video)
- [ ] Testing & Results
- [ ] Conclusion
- [ ] Future Scope
- [ ] References

#### ✅ Presentation Materials

- [ ] PowerPoint file (.pptx)
- [ ] Demo video/screenshots embedded
- [ ] Speaker notes included
- [ ] Backup demo video (separate file)

---

## 📋 Pre-Submission Checklist

### Code Quality

- [ ] All code files have proper comments
- [ ] No hardcoded passwords in submitted files
- [ ] Code runs without errors
- [ ] All dependencies listed in requirements.txt
- [ ] Sample data included for testing

### Documentation

- [ ] Report is well-formatted and professional
- [ ] All diagrams are clear and readable
- [ ] Code snippets are properly highlighted
- [ ] References are complete and properly cited
- [ ] No spelling or grammar errors

### Presentation

- [ ] All slides follow consistent design
- [ ] Demo video is clear and audible
- [ ] Timing is within 20-25 minutes
- [ ] Backup materials prepared
- [ ] Practice presentation at least twice

### Testing

- [ ] Run the tool on fresh system to verify it works
- [ ] Test all features shown in demo
- [ ] Verify all output files are generated
- [ ] Check web interface loads correctly

---

## 📁 File Structure for Submission

```
forensic-timeline-builder-submission.zip
│
├── Report/
│   ├── COURSEWORK_REPORT.pdf          # Main report (convert from .md)
│   └── diagrams/                       # Any additional diagrams
│
├── Code/
│   ├── collector/
│   │   ├── __init__.py
│   │   ├── collect_logs.py
│   │   ├── ssh_hosts.json.example
│   │   └── sample_local_logs/
│   │       └── syslog_sample.log
│   │
│   ├── processor/
│   │   ├── __init__.py
│   │   ├── normalize.py
│   │   ├── timeline_builder.py
│   │   └── parsers/
│   │       ├── __init__.py
│   │       ├── syslog_parser.py
│   │       ├── authlog_parser.py
│   │       └── windows_evtx_parser.py
│   │
│   ├── webui/
│   │   ├── app.py
│   │   ├── templates/
│   │   │   └── timeline.html
│   │   └── static/
│   │       └── timeline.css
│   │
│   ├── run_all.py
│   ├── requirements.txt
│   ├── README.md
│   ├── DOCUMENTATION.md
│   ├── BEGINNER_GUIDE.md
│   └── .gitignore
│
└── Presentation/
    ├── Forensic_Timeline_Builder.pptx  # PowerPoint presentation
    ├── demo_video.mp4                  # Demo recording
    └── screenshots/                    # Demo screenshots
        ├── terminal_output.png
        ├── web_interface.png
        ├── csv_output.png
        └── html_output.png
```

---

## 🎯 How to Create the Submission Package

### Step 1: Convert Report to PDF

**Option A: Using Markdown to PDF converter**

```powershell
# Install pandoc if not already installed
# Then convert
pandoc COURSEWORK_REPORT.md -o COURSEWORK_REPORT.pdf --toc
```

**Option B: Copy to Word and export**

1. Open COURSEWORK_REPORT.md in VS Code
2. Copy content to Microsoft Word
3. Format properly
4. Export as PDF

### Step 2: Create PowerPoint Presentation

Use `PRESENTATION_OUTLINE.md` as your guide:

1. Create new PowerPoint file
2. Follow the 23-slide structure
3. Add screenshots from your system
4. Embed demo video or add screenshots
5. Add speaker notes
6. Save as `Forensic_Timeline_Builder.pptx`

### Step 3: Record Demo Video

**What to record**:

1. Terminal showing `python run_all.py` execution
2. Output files being generated
3. Web interface at http://localhost:8080
4. CSV file opened in Excel
5. HTML file opened in browser

**Tools**:

- Windows: Xbox Game Bar (Win+G) or OBS Studio
- Duration: 2-3 minutes
- Format: MP4
- Resolution: 1080p

### Step 4: Take Screenshots

Capture these screenshots:

1. **Terminal output**: Full execution of run_all.py
2. **Web interface**: Timeline table view
3. **CSV in Excel**: Formatted data
4. **HTML in browser**: Timeline page
5. **File structure**: Project directory

### Step 5: Create Zip Package

```powershell
# Navigate to project directory
cd C:\Users\abhis\Downloads

# Create submission directory
mkdir forensic-timeline-builder-submission
cd forensic-timeline-builder-submission

# Create subdirectories
mkdir Report Code Presentation

# Copy files
# (Copy report PDF to Report/)
# (Copy all code to Code/)
# (Copy presentation files to Presentation/)

# Create zip
Compress-Archive -Path * -DestinationPath ..\forensic-timeline-builder-submission.zip
```

---

## 🎬 Demo Recording Script

### Introduction (30 seconds)

"Hello, I'm [Name] and this is our Forensic Timeline Builder. This tool automates log collection and analysis for system administrators."

### Configuration (30 seconds)

"First, let me show you the configuration file. Here we specify which servers to connect to and which logs to collect."

- Show `ssh_hosts.json.example`

### Execution (1 minute)

"Now, let's run the tool with a single command."

- Execute: `python run_all.py`
- Show terminal output
- Highlight each stage: collection, normalization, export

### Results (1 minute)

"The tool has generated three output formats."

- Show `output/` directory
- Open CSV in Excel
- Open HTML in browser
- Show PDF file

### Web Interface (30 seconds)

"We also have a web interface for interactive viewing."

- Execute: `python webui/app.py`
- Open browser to localhost:8080
- Show timeline table
- Demonstrate search (Ctrl+F)

### Conclusion (30 seconds)

"In just a few minutes, we've collected logs from multiple sources, created a unified timeline, and generated professional reports. Thank you!"

---

## 📊 Grading Criteria Alignment

### Complexity & Functionality (30%)

✅ **Our Project**:

- Multiple modules (collector, processor, web UI)
- Network programming (SSH/SFTP)
- Data processing (Pandas)
- Web development (Flask)
- Multiple parsers
- Error handling
- Multi-format export

### Code Quality (20%)

✅ **Our Project**:

- Modular design
- Comprehensive error handling
- Clear comments and documentation
- Follows Python best practices
- Extensible architecture

### Documentation (20%)

✅ **Our Project**:

- Comprehensive technical report
- User guide (README.md)
- Technical documentation
- Beginner's tutorial
- Code comments
- Presentation materials

### Demo & Presentation (20%)

✅ **Our Project**:

- Working demo
- Clear presentation
- Professional slides
- Video recording
- Q&A preparation

### Innovation & Uniqueness (10%)

✅ **Our Project**:

- Solves real-world problem
- Unique combination of features
- Extensible parser system
- Multiple output formats
- Web interface

---

## ⚠️ Common Mistakes to Avoid

### Report

- ❌ Don't include actual passwords in examples
- ❌ Don't use generic screenshots from internet
- ❌ Don't copy-paste from documentation without attribution
- ❌ Don't submit without proofreading

### Code

- ❌ Don't include `__pycache__` directories
- ❌ Don't include actual log files with sensitive data
- ❌ Don't include `.venv` or virtual environment
- ❌ Don't hardcode file paths specific to your system

### Presentation

- ❌ Don't read slides word-for-word
- ❌ Don't go over time limit
- ❌ Don't assume demo will work (have backup)
- ❌ Don't skip testing your presentation

---

## 📞 Final Checks Before Submission

### 24 Hours Before Deadline

- [ ] Complete all files
- [ ] Test zip file extraction
- [ ] Verify all links work
- [ ] Practice presentation
- [ ] Prepare Q&A answers

### 1 Hour Before Deadline

- [ ] Final proofread of report
- [ ] Test demo one more time
- [ ] Verify zip file size is reasonable
- [ ] Check submission portal is accessible
- [ ] Have backup copy ready

### At Submission

- [ ] Upload to correct portal
- [ ] Verify upload completed
- [ ] Download and verify submitted file
- [ ] Save confirmation email/screenshot
- [ ] Inform team members

---

## 🎓 Presentation Day Checklist

### Equipment

- [ ] Laptop fully charged
- [ ] Backup laptop available
- [ ] USB drive with presentation
- [ ] HDMI/VGA adapter
- [ ] Mouse (optional)

### Files

- [ ] PowerPoint on laptop
- [ ] Backup video file
- [ ] Screenshots folder
- [ ] Code ready to run
- [ ] Web browser bookmarked

### Preparation

- [ ] Arrive 10 minutes early
- [ ] Test projector connection
- [ ] Test audio (if video has sound)
- [ ] Have water available
- [ ] Review notes one last time

---

## 📝 Sample Q&A Responses

**Q: Why did you choose Python?**
A: Python offers excellent libraries for network programming (Paramiko), data processing (Pandas), and web development (Flask). It's also cross-platform and widely used in system administration.

**Q: How does this compare to existing tools like Splunk?**
A: While Splunk is more comprehensive, our tool is lightweight, free, and specifically designed for forensic timeline analysis. It's ideal for small to medium environments or as a quick incident response tool.

**Q: What happens if a server is offline?**
A: The tool logs the error and continues with other servers. This ensures partial data collection rather than complete failure.

**Q: Can it handle real-time monitoring?**
A: Currently, it's designed for batch collection. Real-time monitoring is in our future enhancements roadmap.

**Q: How secure is the SSH connection?**
A: We use Paramiko which implements SSH2 protocol. For production use, we recommend SSH keys instead of passwords.

---

## 🎉 Good Luck!

You have created a comprehensive, professional project that demonstrates:

- ✅ Advanced programming skills
- ✅ Real-world problem solving
- ✅ Professional documentation
- ✅ Practical application

**Remember**: You've built something genuinely useful that solves a real problem for system administrators. Be confident in your presentation!

---

**GitHub Repository**: https://github.com/X-Abhishek-X/forensic-timeline-builder

**Last Updated**: [Date]
