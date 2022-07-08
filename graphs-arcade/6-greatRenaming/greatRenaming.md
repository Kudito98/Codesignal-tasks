<p>Once upon a time, in a kingdom far, far away, there lived a King Byteasar VI. As any king with such a magnificent name, he was destined to leave a trace in history. Unfortunately, imagination wasn't one of Byteasar's strong suits, so the reform he came up with was quite simple: he ordered that all his kingdom's cities should be renamed. He didn't want to come up with new names (as a king, he'd have to remember them all!), so he ordered the cities to swap their names in such a manner that the <code>i<sup>th</sup></code> city would have the name of the city number <code>(i + 1)<sup>th</sup></code>. The last city in the Byteasar's kingdom would, naturally, get the name of the very first city.</p>
<p>The cartographers were not happy with this reform, since they had to redraw all the kingdom's maps. Before the reform, information about all the roads between the cities were stored in the <code>roadRegister</code>. Prior to redrawing any map, they had to start with updating the register. Your task is to find out the state of the updated register.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>roadRegister = [[false, true,  true,  false],
                [true,  false, true,  false],
                [true,  true,  false, true ],
                [false, false, true,  false]]
</code></pre>
<p>the output should be</p>
<pre><code>solution(roadRegister) = [[false, false, false, true ],
                               [false, false, true,  true ],
                               [false, true,  false, true ],
                               [true,  true,  true,  false]]
</code></pre>
<p>Here's how the catalog can be represented before and after the Great Renaming<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/greatRenaming/img/example.jpg?_tm=1624357922944" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean roadRegister</strong></p>
<p>Since cartography has not yet been properly developed in the kingdom, the registers are used instead. A register is stored as a square matrix, with its size equal to the number of cities in the kingdom. If <code>roadRegister[i][j] = true</code>, then there is a road between the <code>i<sup>th</sup></code> and the <code>j<sup>th</sup></code> cities; the road doesn't exist otherwise.</p>
<p>It is guaranteed that there are no looping roads, i.e. roads that lead back to the same city it originated from.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ roadRegister.length ≤ 100</code>,<br />
<code>roadRegister[0].length = roadRegister.length</code>,<br />
<code>roadRegister[i][j] = roadRegister[j][i], i ≠ j</code>,<br />
<code>roadRegister[i][i] = false</code>.</p>
</li>
<li>
<p><strong>[output] array.array.boolean</strong></p>
<p><code>roadRegister</code> after the Great Renaming.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
