<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NCOR Common Core Ontologies Working Group</title>
<style>
body {
  position: relative;
  height: 100vh; 
  margin: 0;
  background: transparent;
  color: #000; /* Black text */
}
body::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('https://raw.githubusercontent.com/johnbeve/NCOR-Test/main/docs/assets/CCO_WG.png');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  opacity: 0.05; /* Lighten the background */
  z-index: -1;
}
h1, h2, p, a, li {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Text shadow for better readability */
}
.custom-color {
  color: #0056b3; 
  transition: color 0.3s; /* Smooth transition for color change */
}
/* Change color when hovering */
.custom-color:hover {
  color: #003580; /* Darker shade of the original color */
}
</style>
</head>
<body>
<h1>NCOR Common Core Ontologies Working Group</h1>

<h2>Common Core Ontologies</h2>
<p>CCO was developed and promoted by <a href="https://scholar.google.com/citations?hl=en&user=JLM7L2EAAAAJ&view_op=list_works&sortby=pubdate" class="custom-color">Ron Rudnicki</a> and is comprised 11 ontologies extending from Basic Formal Ontology that aim to represent and integrate taxonomies of generic classes and relations across all domains.</p>

<h2>NCOR CCO WG</h2>
<p>The aim of the NCOR Common Core Ontologies Working Group (CCOWG) is to cultivate understanding of, provide contributions to, and promote development of the Common Ontology (CCO) suite. The group is comprised of academics, students, and professionals with a common interest in CCO-based domain ontology engineering.</p>
<p>The CCOWG is chaired by <a href="https://www.linkedin.com/in/carterbeaubenson/" class="custom-color">Carter Benson</a> and hold weekly hybrid meetings. Meetings regularly involve discussion of CCO-based projects, such as design pattern refinement, alignment with nearby open-source ontologies, and crafting criteria for what counts as a "mid-level" ontology or ontology suite. Please see the minutes from past meetings below for a better understanding of topics covered.</p>
<p>If you would like to attend CCOWG meetings either in-person or remotely, contact Carter at: carterbe[at]buffalo.edu.</p>

<h2>Minutes</h2>
<h2>UB CCO WG - October 02</h2>
<p><strong>VIEW RECORDING:</strong> <a href="https://fathom.video/share/1e63pjosDY6iwDFepji762yHw51zF-8h">https://fathom.video/share/1e63pjosDY6iwDFepji762yHw51zF-8h</a></p>
<p><strong>Introductions and Meeting Goals @ 0:00</strong><br>
Carter introduced the group's aim to deeply understand CCO through building ontologies. Members shared projects using CCO including sports, Provo mapping, and philosophical methodology.</p>

<p><strong>Mapping Provo Ontology to CCO @ 4:35</strong><br>
Tim detailed progress mapping Provo terms to CCO through relations like effects and is affected by. Debate arose around representing software agents, with Mark confirming their ability as agents in activities.</p>

<p><strong>Modeling Sports and Games in Ontologies @ 19:00</strong><br>
Carter proposed the Reference Ontology of Games in Sports for cross-domain modeling. Discussion critiqued past efforts and sought card/board game ontologies. Matt offered to contribute poker terms to the nascent RooGass ontology.</p>

<p><strong>Conceptualizing Money and Economic Value @ 41:16</strong><br>
Gloria framed money as information carried by documents used as exchange means. Debate explored representing value amid differing economic theories, with money variably seen as information, quality, or grounded in land.</p>

<p><strong>Representing Roles and Memberships Over Time @ 51:06</strong><br>
Carter posed challenges of temporal roles like "manager". Debate touched on mereology, sets, and occupations. Representing players across teams over careers while respecting BFO role restrictions sparked discussion.</p>

<h2>UB CCO WG - October 16</h2>
<p><strong>VIEW RECORDING:</strong> <a href="https://fathom.video/share/B4K7zcYzhxayfghwJ5iJPySDR3Nz1sxo">https://fathom.video/share/B4K7zcYzhxayfghwJ5iJPySDR3Nz1sxo</a></p>
<p><strong>Expected Goals Modeling @ 3:39</strong><br>
Carter presented his initial plans to model expected goals in soccer using CCO, but got distracted by other concepts and relationships needed to fully capture XG.</p>

<p><strong>Conceptual Analysis of Expected Goals Metrics @ 10:07</strong><br>
Carter analyzed how expected goals is discussed and used, identifying it refers to the algorithm, value, quantitative analysis tool, and predictive metric. Differences in company algorithms were noted.</p>

<p><strong>Modeling Expected Goals Concepts in CCO @ 15:16</strong><br>
Carter mapped expected goals concepts to CCO classes and relationships, including the XG algorithm, value, team/player values, and contextual parameters. Discussion focused on database modeling versus real-world capture.</p>

<p><strong>Modeling Individuals and Aggregates in CCO @ 19:21</strong><br>
Carter demonstrated modeling an individual, Lionel Messi, capturing names, roles, qualities, relationships, and statistical data in CCO. The complexity of modeling aggregates like team values was noted.</p>

<p><strong>Design Patterns in CCO Modeling @ 27:13</strong><br>
Carter showcased design patterns for modeling names, roles, temporal events, statistical profiles, and more using Messi's career as an example. This revealed both effective modeling strategies and open questions around CCO usage.</p>

<p><strong>Process Profiles and Temporal Modeling in CCO @ 1:00:08</strong><br>
Carter delved into temporal modeling of shots and matches using process profiles, instants, and participation, though object properties for certain relationships require clarification.</p>

<p><strong>Discussion of Next Steps @ 1:13:42</strong><br>
The group discussed next steps, with Carter advising focus on core CCO usage and common ground between ontologies. Matt confirmed readiness to present the poker ontology in 3 weeks.</p>

<h2>UB CCO WG - November 06</h2>
<p><strong>VIEW RECORDING:</strong> <a href="https://fathom.video/share/PsAh2JuxWSrg1-B7GZ-TxD_bdz142Mvc">https://fathom.video/share/PsAh2JuxWSrg1-B7GZ-TxD_bdz142Mvc</a></p>
<p><strong>Introductions and Ice Cream Ontology Presentation @ 0:00</strong><br>
Cameron presented an ice cream ontology modeling processes, artifacts, and roles. Discussion focused on differentiating classes and instances, and ensuring object properties align with CCO.</p>

<p><strong>Discussion of Functions, Roles, and Agency in Organisms and Artifacts @ 6:00</strong><br>
Debate emerged around Barry's rejection of human functions, and whether roles apply to biological relations. Intentionality's relation to functions and dispositions was probed, with disagreement around what qualifies as an agent.</p>

<p><strong>Philosophical Discussion of Organization, Functions, and Intentionality @ 34:39</strong><br>
Discussion delved into philosophical complexities of organization and functions, questioning teleology's role in demarcating functions from dispositions. Intentionality's relation to mental dispositions was considered.</p>

<p><strong>Planning Future Presentations and Identifying Modeling Issues @ 50:49</strong><br>
Presentations were scheduled. Tim proposed exploring techniques to simplify CCO representations and enable bidirectional translation between simple and complex forms.</p>

<p><strong>Modeling Challenges like Sequential Events and Object Properties @ 52:22</strong><br>
Adam highlighted difficulties representing sequential events. Discussion addressed improving CCO's expressivity through "convenience relations" and automated expansion/contraction of representations.</p>

<h2>UB CCO WG - November 13</h2>
<p><strong>VIEW RECORDING:</strong> <a href="https://fathom.video/share/JZsrc4aHmK49sFmo2VEW6Mw66TzDUSwu">https://fathom.video/share/JZsrc4aHmK49sFmo2VEW6Mw66TzDUSwu</a></p>
<p><strong>Introduction to Poker Ontology Project @ 0:00</strong><br>
Adam and Matt presented their ontology for modeling poker gameplay. They aimed to represent both live and online poker using BFO and CCO terms when possible. The ontology's scope included Texas hold'em but could extend to other variants.</p>

<p><strong>Modeling Player Actions and Betting Rounds @ 0:29</strong><br>
Players have options to check, call, raise or fold depending on prior actions. Bets are instances measured by a ratio mice. Players participate through roles like first or now acting.</p>

<p><strong>Discussion of Ontology Design and Relation to BFO/CCO @ 9:00</strong><br>
Carter provided feedback to clarify distinctions between acts, roles and processes using consistent labels. Classes directly connecting to values require intermediaries. Representing modal properties poses challenges within constraints.</p>

<p><strong>Modeling Chips, Chip Stacks, and Betting Amounts @ 12:31</strong><br>
Chips are information bearing artifacts with denominations and values measured by interval mice. Chip stacks aggregate chips as object aggregates. Bet amounts input to algorithms tracking growing pot sizes.</p>

<p><strong>Modeling the Sequence of a Poker Hand @ 19:16</strong><br>
A hand comprises intervals for actions like anteing and dealing within a game. Players transition between roles like first and now acting along the pre-flop sequence to the next street.</p>

<p><strong>Questions and Feedback on Ontology Design @ 28:10</strong><br>
Carter recommends limiting scope to hit targets. Discussions addressed representing rules and causal relationships. Participants agreed the ontology quality exceeded expectations for depth achieved within BFO/CCO.</p>

<h2>UB CCO WG - November 20</h2>
<p><strong>VIEW RECORDING:</strong> <a href="https://fathom.video/share/e58MV2DbGNx7tQgPu1-9SFoYxUHpVG9D">https://fathom.video/share/e58MV2DbGNx7tQgPu1-9SFoYxUHpVG9D</a></p>
<p><strong>Introduction and Meeting Overview @ 0:00</strong><br>
Carter-Beau outlined the meeting agenda, noting Tim's planned presentation on shortcut properties and James' upcoming basketball ontology work.</p>

<p><strong>Modeling Age in CCO Using Information Entities @ 0:50</strong><br>
Tim demonstrated CCO's complex age modeling using information entities, motivating a simpler approach for practical data use. Debate ensued around measurement roles and information-bearing distinctions.</p>

<p><strong>Summary of Past CCO Meeting Presentations @ 2:00</strong><br>
Carter-Beau recapped members' ontology development work, from soccer to poker to ice cream. Alec tentatively agreed to present his crime ontology in two weeks.</p>

<p><strong>Proposed Shortcut Property to Simplify Age Representation @ 12:32</strong><br>
Tim proposed a shortcut property to cut triples, sparking discussion on balancing simplicity and semantic precision while maintaining translatability between representations. Views differed on roles of qualities versus information entities.</p>

<h2>UB CCO WG - November 27</h2>
<p><strong>VIEW RECORDING:</strong> <a href="https://fathom.video/share/TWDDsfH5rZz7yVfCpo2sxHsXFXuhBwvs">https://fathom.video/share/TWDDsfH5rZz7yVfCpo2sxHsXFXuhBwvs</a></p>
<p><strong>Basketball Ontology Overview @ 0:00</strong><br>
James presented his initial taxonomy for modeling basketball actions and statistics using BFO and CCO classes. Participants engaged James to refine his conceptualization of shots, scoring, and the referee's role in judging outcomes.</p>

<p><strong>Modeling a Steph Curry Three-Point Shot @ 4:12</strong><br>
James detailed how Steph Curry's three-point shot attempt would be represented, incorporating roles, locations, processes and agents. Discussions centered on differentiating shots from other scoring acts and the referee's judgment in scoring.</p>

<p><strong>Roles and Matches @ 17:57</strong><br>
James outlined player and team roles like point guard and how matches involve groups of agents. Participants did not raise issues with this conceptualization.</p>

<p><strong>The Basketball Court as a Site @ 19:24</strong><br>
James modeled the court as a site with zones impacting scoring values. Discussions clarified boundary lines as fiat parts demarcating scoring rules.</p>

<p><strong>Intentionality in Shots and Scoring @ 24:00</strong><br>
Debates addressed distinguishing intended acts from consequences, planning from intending, and tracking objective outcomes versus records. Participants provided examples complicating the modeling of intentionality.</p>

<p><strong>Future Extensions and Improvements @ 45:10</strong><br>
Proposed additions centered on agents like scorekeepers and processes like reviews. Participants emphasized uncoupling shots from scoring and representing temporal and judgmental aspects to address edge cases.</p>

UB CCO WG - December 04
VIEW RECORDING: https://fathom.video/share/ktvtnkzCWi7_8zH_7fgHdFx8VqEB8eox
Introduction @ 0:00

Carter-Beau introduces the meeting attendees and notes the meeting is being recorded.

Modeling card suits and properties @ 15:28

Adam shares his work modeling card suits, suitedness, and card properties with Matt. They discuss representing suits as nominal measurements inhering in cards and representing suit values as card text literals. Debate focuses on suit ontology and its relationship to cards.

Representing card hands and poker concepts @ 42:41

Adam demonstrates modeling poker hands like straights by assigning ranks and outranking relations to cards based on their symbols. Restriction classes are used to define hand compositions. Discussion centers on fine-grained modeling required to represent poker rules and evaluations.

Relationships between qualities, roles, and measurements @ 1:12:18

A debate emerges around whether qualities like suitedness or ranks are directly measured, or if they ground roles which are actually measured. Context is key, as roles can shift between contexts. Qualities may ground shiftable roles rather than being directly measured. Speech acts are recognized as integral to some games.

How's this? I aimed to hit the key points you outlined - including specifics, viewpoints, implications and solutions - while keeping each summary concise yet dense with context and meaning. Please let me know if any part needs more work or clarification.

<h2>UB CCO WG - December 18</h2>
<p><strong>VIEW RECORDING:</strong> <a href="https://fathom.video/share/U_oSWnuCsMQ1ivRb6xziy2fXztTJfkHZ">https://fathom.video/share/U_oSWnuCsMQ1ivRb6xziy2fXztTJfkHZ</a></p>
<p><strong>Introductions and Meeting Overview @ 0:00</strong><br>
Carter introduced the group members and their backgrounds, noting they would discuss individual ontology projects, Common Core Ontology topics, and planning future meetings. John joined to learn applied ontology.</p>

<p><strong>Discussion of Ontology Modeling Concepts like GDC, SDC, and Information Content Entities @ 12:53</strong><br>
Adam explained GDCs depend on but can exist without other entities, unlike SDCs. Debate focused on distinguishing processes, GDCs describing them, and information about them.</p>

<p><strong>Debate Over Whether Patterns of Behavior Are Processes, GDCs, or Information Content Entities @ 48:17</strong><br>
Viewpoints differed on whether patterns of behavior were processes occurring, GDCs describing recurring processes, or information we have due to interest in patterns. The nature of the topic encompasses all three perspectives.</p>

<p><strong>Example of How Eating Chopsticks Could be Modeled as a Process, Pattern, or Information and the Relationship Between These Perspectives @ 54:33</strong><br>
Adam's habit of rubbing chopsticks exemplified the intertwined nature of a recurring process, its description, and our information about it. The group agreed distinctions require considering what information is about in the real world.</p>

<h2>Common Core Ontology Resources</h2>
<p>The Common Core Ontology suite is a widely-used open-source project with helpful documentation to guide development across its numerous domains and extensions. Resources include:</p>
<ul>
  <li><a href="https://github.com/CommonCoreOntology/CommonCoreOntologies" class="custom-color">Common Core Ontologies Github Repository</a></li>
  <li><a href="https://www.nist.gov/system/files/documents/2021/10/14/nist-ai-rfi-cubrc_inc_004.pdf" class="custom-color">Overview of Common Core Ontologies</a></li>
  <li><a href="https://www.nist.gov/system/files/documents/2021/10/14/nist-ai-rfi-cubrc_inc_003.pdf" class="custom-color">Modeling Information with Common Core Ontologies</a></li>
  <li><a href="https://philarchive.org/archive/COXTSD-2" class="custom-color">An Overview of the Common Core Space Domain Ontologies</a></li>
  <li><a href="https://philpapers.org/archive/MORJDO.pdf" class="custom-color">Joint Doctrine Ontology</a></li>
  <li><a href="https://www.youtube.com/watch?v=ai4YdLiCGNM" class="custom-color">How to Handle Data about What Does Not Exist</a></li>
</ul>

</body>
</html>
