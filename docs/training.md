<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NCOR Certificate Pathways</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            position: relative;
        }
        body::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url('https://raw.githubusercontent.com/johnbeve/NCOR-Test/main/docs/assets/ncor-pathways.png');
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
            opacity: 0.1;
            z-index: -1;
        }
        header h1 {
            margin: 0;
            color: white;
        }
        main {
            padding: 20px;
            position: relative;
            z-index: 2;
        }
        #intro, #open-source {
            background: #f9f9f9;
            padding: 20px;
            text-align: center;
        }
        .siema {
            margin: 20px 0;
            overflow: hidden;
            width: 100%;
        }
        .siema .card {
            min-width: 100%;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            margin: 10px;
            padding: 20px;
            text-align: center;
        }
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .card-container .card {
            background-color: #003366;
            color: white;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            border: 2px solid #003366;
        }
        .card-container .card::after {
            content: "";
            position: absolute;
            top: 5px;
            bottom: 5px;
            left: 5px;
            right: 5px;
            border: 2px solid white;
            border-radius: 8px;
            pointer-events: none;
        }
        .card h3 {
            margin-top: 0;
        }
        button {
            padding: 10px 20px;
            margin: 5px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:focus {
            outline: none;
        }
        .top-image {
            width: 100%;
            display: block;
        }
        @media (max-width: 600px) {
            .card {
                flex-basis: auto;
            }
        }
        .dropdown {
            position: relative;
        }
        .dropdown-toggle {
            position: relative;
            cursor: pointer;
        }
        .dropdown-header p {
            margin-bottom: 0;
        }
        .dropdown-content {
            display: none;
            background: #003366;
            color: white;
            margin-top: 10px;
            padding: 10px;
            border-radius: 5px;
            border: 2px solid #003366;
            text-align: left;
        }
        .content-block, .dropdown-content {
            animation: none;
            opacity: 1;
            transform: none;
        }
        .dropdown-active .dropdown-content {
            display: block;
        }
        .dropdown-active .dropdown-header {
            display: none; /* Hide header when active */
        }
        @keyframes fadeInRight {
            0% {
                opacity: 0;
                transform: translateX(20px);
            }
            100% {
                opacity: 1;
                transform: translateX(0);
            }
        }
        /* Style for content blocks */
        .content-block {
            opacity: 0;
            transform: translateX(0px);
            animation-fill-mode: forwards; 
            cursor: pointer;
        }
        .arrow {
            display: block;
            position: relative;
            bottom: -20px;  /* Position it outside the dropdown */
            left: 50%;
            transform: translateX(-50%); /* Center the arrow */
            transition: transform 0.3s ease-in-out;
        }
        .dropdown-active .arrow {
            transform: rotate(180deg) translateX(-50%);
        }
        /* Animation when dropdown is active */
        .dropdown-active .content-block {
            animation: fadeInRight 0.5s ease-out forwards;
        }
        /* Delay each content block's animation */
        .dropdown-active .content-block:nth-child(1) {
            animation-delay: 0.2s; /* Adjust timing as needed */
        }
        .dropdown-active .content-block:nth-child(2) {
            animation-delay: 0.4s; /* Each subsequent block has a longer delay */
        }
        .dropdown-active .content-block:nth-child(3) {
            animation-delay: 0.6s; /* Each subsequent block has a longer delay */
        }
        .dropdown-active .content-block:nth-child(4) {
            animation-delay: 0.8s; /* Each subsequent block has a longer delay */
        } 
    </style>
</head>
<body>
    <header><center><h1>NCOR Certificate Pathways</h1></center></header>
    <main>
    <section id="foundational">
        <h2><b>Foundational Certificates</b></h2>
        <p>Explore ontology engineering concepts, technologies, and the semantic web stack that can facilitate their development.</p>
        <div class="card-container">
            <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title">BFO: Basic Formal Ontology Practitioner</h3>
                        <p>Learn the basics of BFO classes and relations, applications, and design patterns.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p>The BFO Practitioner Certificate introduces students to the fundamentals of modeling data with the Basic Formal Ontology (BFO), a top-level architecture used by over 500 ontology and knowledge graph projects across the world. Students gain hands-on modeling experiences, working with subject-matter experts on active open-source projects leveraging BFO. Additionally, students will learn the philosophical and practical motivations for the distinctions drawn in BFO. This certificate course covers necessary building blocks for mastering differences and similarities across alternative top-level ontology architectures as well as for leveraging open-source ontologies to model specific domains, such as biomedicine, cyber security, climate change, and immigration, among many others. Throughout the course, students will learn to develop, curate, validate, and implement BFO in support of enterprise solutions.</p>
                    </div>
                    <div class="content-block">
                        <center><h4>Duration</h4></center>
                        <p>8 Hours</p>
                    </div>
                    <div class="content-block">
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li>Top-Level Principles of BFO</li>
                            <li>The BFO Hierarchy</li>
                            <li>Formal Implementations of BFO</li>
                            <li>Translating from Natural Language into BFO</li>
                            <li>Implementing BFO-Conformant Design Patterns</li>
                            <li>Extending BFO by Downward Population</li>
                            <li>Validating Extensions of BFO</li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li>Individuals responsible for articulating the benefits of leveraging BFO to others</li>
                            <li>Individuals interested in gaining hands-on training modeling with BFO</li>
                            <li>Knowledge representation, Ontology or Data Architects/Engineers</li>
                            <li>SysOps Administrators</li>
                            <li>Existing users of BFO or extensions of BFO</li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
        </div>
        <div class="card-container">
            <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title"><h3>Ontology Engineer (ONE)</h3>
                        <p>Develop expertise with standard ontology engineering best practices, tools, and modeling strategies.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p>The Ontology Engineer Certificate introduces students to the fundamentals of ontology engineering, focused on the creation, updating, maintaining, and validating of ontologies and knowledge graphs in contemporary system architectures. This course provides students hands-on training to master the semantic web stack, equipping students with the competency needed to integrate and curate ontologies effectively. This certificate serves as a stepping stone for certificates covering specialized topics such as optimized information extraction, semantic web devOps best practices, description logic, and cybersecurity related to the semantic web.</p>
                        <center><h4>Duration</h4></center>
                    </div>
                    <div class="content-block">
                        <p>12 Hours</p>
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li>RDF, RDFS, and a zoo of W3C standards</li>
                            <li>OWL2 Full, OWL2 DL Direct Semantics, and OWL Profiles</li>
                            <li>Principles of Version Control using GitHub</li>
                            <li>Open-Source CI/CD tools for ontology development, e.g., Protege, ROBOT, OnTop, GraphDB</li>
                            <li>Extraction and Validation with the Semantic Web Stack, e.g., SPARQL, SHACL</li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li>Individuals using or interested in leveraging semantic web technologies in existing workflows</li>
                            <li>Knowledge representation, Ontology or Data Architects/Engineers</li>
                            <li>Existing users of BFO or extensions of BFO</li>
                            <li>DevOps and SysOps Administrators</li>
                            <li>Software Developers</li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
        </div>
    </section>
    <section id="associate">
        <h2><b>Associate Certificates</b></h2>
        <p>Explore ontology engineering concepts, technologies, and the semantic web stack that can facilitate their development.</p>
        <div class="card-container">
            <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title">Knowledge Extraction Specialist (KES)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p></p>
                        <center><h4>Duration</h4></center>
                    </div>
                    <div class="content-block">
                        <p>12 Hours</p>
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
        </div>
        <div class="card-container">
             <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title">Semantic Web DevOps Engineer (SWD)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p></p>
                        <center><h4>Duration</h4></center>
                    </div>
                    <div class="content-block">
                        <p>12 Hours</p>
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
            <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title">Top-Level Ontology Engineer (TLO)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p></p>
                        <center><h4>Duration</h4></center>
                    </div>
                    <div class="content-block">
                        <p>12 Hours</p>
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
                <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title">Mid-Level Ontology Engineer (MLO)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p></p>
                        <center><h4>Duration</h4></center>
                    </div>
                    <div class="content-block">
                        <p>12 Hours</p>
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
        </div>
    </section>
    <section id="specialist">
        <h2><b>Specialist Certificates</b></h2>
        <p>Master specialized ontology engineering topics, such as cyber security and referent-tracking.</p>
        <div class="card-container">
            <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title">Semantic Web Security Specialist (SWS)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p></p>
                        <center><h4>Duration</h4></center>
                    </div>
                    <div class="content-block">
                        <p>12 Hours</p>
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
            <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title">Referent Tracking Specialist (RTE)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p></p>
                        <center><h4>Duration</h4></center>
                    </div>
                    <div class="content-block">
                        <p>12 Hours</p>
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
            <article class="card dropdown">
                <div class="dropdown-toggle">
                    <div class="dropdown-header">
                        <h3 class="dropdown-title">Description Logic Specialist (DLS)</h3>
                        <p>Deep-dive into ontology engineering technologies.</p>
                    </div>
                <span class="arrow">&#9662;</span>
                </div>
                <div class="dropdown-content">
                    <div class="content-block">
                        <center><h4>Overview</h4></center>
                        <p></p>
                        <center><h4>Duration</h4></center>
                    </div>
                    <div class="content-block">
                        <p>12 Hours</p>
                        <h4>Course Objectives</h4>
                        <p>In this course, you will develop competency with the following topics:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                    <div class="content-block">
                        <center><h4>Intended Audience</h4></center>
                        <p>This course is intended for:</p>
                        <ul>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                            <li></li>
                        </ul>
                    </div>
                </div>
            <span class="arrow">&#9662;</span>
            </article>
        </div>
    </section>
    <section id="open-source">
        <h2>Open-Source Courses</h2>
        <p>Explore our collection of open-source training materials to enhance your skills.</p>
        <div class="siema">
            <div class="card">
                <h3><a href="http://ncorwiki.buffalo.edu/index.php/Applied_Ontology,_Spring_2022">Applied Ontology</a></h3>
                <p>Dive into applied ontology with open-source tools.</p>
            </div>
            <div class="card">
                <h3><a href="/index.php/Intelligence_Analysis:_A_Crash_Course">Intelligence Analysis: A Crash Course</a></h3>
                <p>Learn how to deploy intelligence analytics effectively using open-source software.</p>
            </div>
            <div class="card">
                <h3><a href="http://ncorwiki.buffalo.edu/index.php/Biomedical_Ontology_2016">Biomedical Ontology</a></h3>
                <p>Dive into biomedical ontology development with open-source tools.</p>
            </div>
        </div>
        <button class="prev">Previous</button>
        <button class="next">Next</button>
    </section>
    </main>
<script src="https://cdn.jsdelivr.net/npm/siema@1.5.1/dist/siema.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        let mySiema = new Siema({
            selector: '.siema',
            duration: 200,
            easing: 'ease-out',
            perPage: { 768: 2, 1024: 3 },
            startIndex: 0,
            draggable: true,
            multipleDrag: true,
            threshold: 20,
            loop: true,
        });
        document.querySelector('.prev').addEventListener('click', () => mySiema.prev());
        document.querySelector('.next').addEventListener('click', () => mySiema.next());
        document.querySelectorAll('.dropdown .arrow').forEach(function(arrow) {
            arrow.addEventListener('click', function(event) {
                event.stopPropagation(); // Prevent event from bubbling up
                // Toggle the 'dropdown-active' class on the closest parent with the class 'dropdown'
                this.closest('.dropdown').classList.toggle('dropdown-active');
            });
        });
    });
</script>

</body>
</html>