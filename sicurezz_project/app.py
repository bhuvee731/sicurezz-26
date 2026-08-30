from flask import Flask, render_template, jsonify, abort

app = Flask(__name__)

SYMPOSIUM_DATA = {
    "name": "SICUREZZ'26",
    "department": "Department of Cyber Security",
    "college": "K.L.N. College of Engineering (KLNCE)",
    "date": "September 3, 2026",
    "registration_fee": "₹250 / Member",
    "cash_prize": "₹10,000",
    "google_form_url": "https://forms.gle/zGX8EJmw5kk8qVtn9",
    "contact_email": "SICUREZZ26@gmail.com",
    "contact_number": "+91 7339487006",
    
    "principal":"Dr. A. V. Ram Prasad (KLNCE)",
    "convenor": "Dr. J. S. Kanchana (Prof & HEAD/CSE(CS))",
    "coordinator":"Mrs. T. Suganya (AP/CSE(CS))",

    "student_incharge": [
        {"role": "President", "name": "Vishal.M"},
        {"role": "Vice President", "name": "Joshika.K.G"},
        {"role": "Secretary", "name": "Vishnu Raj.P"},
        {"role": "Joint Secretary", "name": "Navaneetha Kannan.S"},
        {"role": "Treasurer", "name": "Sathiesh.R.S.A"}
    ],
    
    "events": {
        "prompt-craft": {
            "id": "prompt-craft",
            "title": "PROMPT CRAFT",
            "category": "Technical",
            "tagline": "Flutter App Development Challenge",
            "venue": "Security Lab 2",
            "short_desc": "Design and develop innovative mobile applications in Flutter using AI-powered development tools.",
            "description": "PROMPT CRAFT is a Flutter App Development Challenge that encourages participants to design and develop innovative mobile applications within a limited time using the Flutter framework. Participants may leverage AI-powered development tools to enhance productivity, improve UI/UX, and accelerate coding.",
            "rules": [
                "Teams may consist of 1-2 participants.",
                "Participants must develop the application using Flutter.",
                "AI tools (ChatGPT, Gemini, GitHub Copilot, etc.) are permitted to assist with development.",
                "The application must be created during the event. Pre-developed projects are not allowed.",
                "Internet access is allowed only for documentation, packages, and AI assistance.",
                "Participants must submit both the Flutter source code and a working APK before the deadline.",
                "Each team will have 3–5 minutes to demonstrate their application.",
                "Any form of plagiarism or copying from other teams will result in disqualification.",
                "The judges' decision will be final and binding.",
                "Maintain professional conduct and respect fellow participants throughout the event."
            ],
            
        },
        "nova-ctf": {
            "id": "nova-ctf",
            "title": "NOVA CTF",
            "category": "Technical",
            "tagline": "Capture The Flag Cybersecurity Challenge",
            "venue": "Security Lab 1",
            "short_desc": "Solve security challenges, test Linux terminal skills, cryptography, and exploit target machines.",
            "description": "Capture The Flag (CTF) is a cybersecurity competition where participants solve security-related challenges to find hidden 'flags' (unique strings of text). These challenges test skills in areas such as Bash/Linux terminal usage, cryptography, and exploiting intentionally misconfigured machines (e.g., Metasploitable).",
            "rules": [
                "Attack only the systems and targets included in the CTF scope.",
                "Follow all rules and instructions provided by the organizers.",
                "Do not perform Denial-of-Service (DoS/DDoS) attacks.",
                "Do not attack, disrupt, or interfere with other participants.",
                "Do not share flags, solutions, or hints unless explicitly allowed.",
                "Do not target systems outside the CTF environment.",
                "Respect the competition's time limits and submission rules.",
                "Maintain ethical behavior and good sportsmanship."
            ],
            "prerequisites": [
                "Laptop with VirtualBox (Kali Linux .iso installed).",
                "Tools will be provided in the drive link."
            ]
        },
        "byte-horizon": {
            "id": "byte-horizon",
            "title": "BYTE HORIZON",
            "category": "Technical",
            "tagline": "3-Round Technical & Coding Challenge",
            "venue": "Security Lab 3",
            "short_desc": "Test your fundamentals, analytical logical riddles, and practical coding/SQL queries.",
            "description": "BYTE HORIZON is a three-round technical event designed to test participants' technical knowledge, logical thinking, and programming skills. The competition progresses from fundamental concepts to analytical problem-solving and finally to practical coding and SQL challenges.",
            "rounds": [
                "Round 1: NAIL THE BASICS (20 Mins, multiple-choice questions covering various computer science topics.)",
                "Round 2: LOGIC-AH LOCK PANNU (20 Mins, Challenges participants with logic-based riddles that require analytical thinking and problem-solving without multiple-choice options.)",
                "Round 3: THE FINAL COMPILE (30 Mins, practical programming and SQL database queries)"
            ],
            "rules": [
                "Participants must follow all instructions provided by the event coordinators.",
                "The decision of the organizers will be final.",
                "Any form of malpractice or unfair means will lead to disqualification.",
                "Mobile phones and unauthorized materials are strictly prohibited.",
                "Participants must complete each round within the allotted time.",
                "Only qualified participants will proceed to the next round.",
                "Desktop systems will be provided by the organizers."
            ],
            "prerequisites": [
                "No personal laptop is required.",
                "Report to venue 15 minutes before the event begins."
            ]
        },
        "vettaiyaadu-vilaiyaadu": {
            "id": "vettaiyaadu-vilaiyaadu",
            "title": "Vettaiyaadu Vilaiyaadu",
            "category": "Non-Technical",
            "Status" :"Reistraion Closed",
            "tagline": "Campus-Wide Treasure Hunt",
            "venue": "Mechanical Seminar Hall",
            "short_desc": "A 3-stage treasure hunt testing intelligence, speed, and campus observation.",
            "description": "A fun-filled high-stakes campus treasure hunt featuring preliminary quizzes, physical item collection around college grounds, and tactical sequential clue solving.",
            "rounds": [
                "Round 1: Quiz - Movies, songs, reasoning & memory (15 Questions, 10 Mins)",
                "Round 2: Find the Items - Hunt 15 random items on campus (20 Mins)",
                "Round 3: Secret Finder - Solve 7 clues to uncover the ultimate 8th treasure (30 Mins)"
            ],
            "rules": [
                "Each team must consist of 2 participants only.",
                "Participants must follow all instructions from coordinators.",
                "Mobile phone usage is strictly prohibited during Round 1."
            ]
        },
        "cinema-patti": {
            "id": "cinema-patti",
            "title": "Cinema Patti",
            "category": "Non-Technical",
            "tagline": "Cinephile & Media Quiz",
            "venue": "PG Conference Hall",
            "short_desc": "Prove your Tamil cinema expertise across movie guesses, song translations, and live pictionary.",
            "description": "An engaging multi-round event for movie lovers testing dialogue recognition, missing song lyrics, audio translations, and drawing-based pictionary.",
            "rounds": [
                "Round 1: Preliminary - Guess the Movie & Missing Song Lines",
                "Round 2: Semi-Final - Find the meme & Song Translation",
                "Round 3: Final - Pictionary (Identify movies/songs from visual sketches)"
            ],
            "rules": [
                "Each team must consist of 2 participants only.",
                "Judges' decision will be final."
            ]
        },
        "adzapper": {
            "id": "adzapper",
            "title": "Adzapper",
            "category": "Non-Technical",
            "tagline": "Marketing, Observation & Dumb Charades",
            "venue": "Security Lab 1 ",
            "short_desc": "Test brand observation, video details, and silent advertisement gestures.",
            "description": "AdZapper is an advertisement-based team event designed to test brand knowledge, video observation, and acting gestures without speaking names or slogans.",
            "rounds": [
                "Welcome Event – Jingle Jam: Audio Guess Challenge; identify the brand and product from advertisement audio. This is non-elimination and its score is not added to the final result.",

                "Round 1: Brand Blitz Quiz: MCQs on brands, logos, taglines, products, advertisements, mascots, and marketing concepts. 1 point per correct answer, no negative marking.",
                "Round 2: Ad Detective: Watch a TV advertisement for 10 seconds, then answer questions based on what was shown. The combined Round 1 + Round 2 scores determine the Top 4 for the finale.",
                "Round 3: Puzzle Rush: Top teams solve five advertising-themed puzzles inside a Puzzle Box in order. Bonus points are 50 / 40 / 30 for 1st / 2nd / 3rd.",
                "Winner: Scores from all three competitive rounds are combined to declare the AdZap Champion."
            ],
            
            "rules": [
                "Each team must consist of 2 participants.",
                "Mobile phones, internet access, and smart devices are strictly prohibited during the competition."
            ]
        }
    },

    "workshop": {
        "title": "AI with Cyber Security",
        "description": "An intensive hands-on workshop focused on leveraging Artificial Intelligence models for threat detection, defensive automation, and security analytics.",
    }
}

@app.route("/")
def home():
    return render_template("index.html", data=SYMPOSIUM_DATA)

@app.route("/event/<event_id>")
def event_detail(event_id):
    event = SYMPOSIUM_DATA["events"].get(event_id)
    if not event:
        abort(404)
    return render_template("event_detail.html", event=event, data=SYMPOSIUM_DATA)

if __name__ == "__main__":
    app.run(debug=True, port=5005)