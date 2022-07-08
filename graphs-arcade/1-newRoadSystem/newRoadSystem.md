<p>Once upon a time, in a kingdom far, far away, there lived a King Byteasar I. As a kind and wise ruler, he did everything in his (unlimited) power to make life for his subjects comfortable and pleasant. One cold evening a messenger arrived at the king's castle with the latest news: all kings in the Kingdoms Union had started enforcing traffic laws! In order to not lose his membership in the Union, King Byteasar decided he must do the same within his kingdom. But what would the citizens think of it?</p>
<p>The king decided to start introducing the changes with something more or less simple: change all the roads in the kingdom from two-directional to one-directional (one-way). He personally prepared the <code>roadRegister</code> of the new roads, and now he needs to make sure that the road system is convenient and there will be no traffic jams, i.e. each city has the same number of incoming and outgoing roads. As the Hand of the King, you're the one who he has decreed must check his calculations.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For</p>
<pre><code>roadRegister = [[false, true,  false, false],
                [false, false, true,  false],
                [true,  false, false, true ],
                [false, false, true,  false]]
</code></pre>
<p>the output should be<br />
<code>solution(roadRegister) = true</code>.</p>
<p>The cities will be connected as follows:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/newRoadSystem/img/example1.jpg?_tm=1624662607246" alt /></p>
<p>Cities <code>0</code>, <code>1</code> and <code>3</code> (0-based) have one incoming and one outgoing road, and city <code>2</code> has two incoming and two outgoing roads. Thus, the output should be <code>true</code>.</p>
</li>
<li>
<p>For</p>
<pre><code>roadRegister = [[false, true,  false, false, false, false, false],
                [true,  false, false, false, false, false, false],
                [false, false, false, true,  false, false, false],
                [false, false, true,  false, false, false, false],
                [false, false, false, false, false, false, true ],
                [false, false, false, false, true,  false, false],
                [false, false, false, false, false, true,  false]]
</code></pre>
<p>the output should be<br />
<code>solution(roadRegister) = true</code>.</p>
<p>The cities will be connected as follows:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/newRoadSystem/img/example2.jpg?_tm=1624662607493" alt /></p>
<p>Each city has one incoming and one outgoing road.</p>
</li>
<li>
<p>For</p>
<pre><code>roadRegister = [[false, true,  false],
                [false, false, false],
                [true,  false, false]]
</code></pre>
<p>the output should be<br />
<code>solution(roadRegister) = false</code>.</p>
<p>The cities will be connected as follows:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/newRoadSystem/img/example3.jpg?_tm=1624662607742" alt /></p>
<p>City <code>1</code> has one incoming and no outgoing roads, and city <code>2</code> has one outgoing and no incoming roads.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean roadRegister</strong></p>
<p>Since cartography has not yet been properly developed in the kingdom, the registers are used instead. A register is stored as a square matrix, with its size equal to the number of cities in the kingdom. If <code>roadRegister[i][j] = true</code>, then there is a road from the <code>i<sup>th</sup></code> to the <code>j<sup>th</sup></code> city; the road doesn't exist otherwise.</p>
<p>It is guaranteed that there are no looping roads, i.e. roads that lead back to the same city it originated from.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ roadRegister.length ≤ 100</code>,<br />
<code>roadRegister[0].length = roadRegister.length</code>,<br />
<code>roadRegister[i][i] = false</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the new road system is good enough, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
