<p>Once upon a time, in a kingdom far, far away, there lived a King Byteasar II. There was nothing special about him or his kingdom. As a mediocre ruler, he preferred hunting and feasting over doing anything about his kingdom's prosperity.</p>
<p>Luckily, his adviser, the wise magician Bitlin, worked for the kingdom's welfare day and night. However, since there was no one to advise him, he completely forgot about one important thing: the roads! Over the years most of the two-way roads built by Byteasar's predecessors were forgotten and no longer traversable. Only a few <code>roads</code> can still be used.</p>
<p>Bitlin wanted each pair of cities to be connected, but couldn't find a way to figure out which roads are missing. Desperate, he turned to his magic crystal ball for help. The crystal showed him a programmer from the distant future: you! Now you're the only one who can save the kingdom. Given the existing <code>roads</code> and the number of <code>cities</code> in the kingdom, you should use the most modern technologies and find out which roads should be built again to connect each pair of cities. Since the crystal ball is quite old and meticulous, it will only transfer the information if it is sorted properly.</p>
<p>The roads to be built should be returned in an array sorted <a href="keyword://lexicographical-order-for-arrays" target="_blank">lexicographically</a>, with each road stored as <code>[<i>city<sub>i</sub></i>, <i>city<sub>j</sub></i>]</code>, where <code><i>city<sub>i</sub></i> &lt; <i>city<sub>j</sub></i></code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>cities = 4</code> and <code>roads = [[0, 1], [1, 2], [2, 0]]</code>,<br />
the output should be<br />
<code>solution(cities, roads) = [[0, 3], [1, 3], [2, 3]]</code>.</p>
<p>See the image below: the existing roads are colored black, and the ones to be built are colored red.<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/roadsBuilding/img/example.jpg?_tm=1624665487655" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer cities</strong></p>
<p>The number of cities in the kingdom.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ cities ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer roads</strong></p>
<p>Array of roads in the kingdom. Each road is given as a pair <code>[<i>city<sub>i</sub></i>, <i>city<sub>j</sub></i>]</code>, where <code>0 ≤ <i>city<sub>i</sub></i>, <i>city<sub>j</sub></i> &lt; cities</code> and <code><i>city<sub>i</sub></i> ≠ <i>city<sub>j</sub></i></code>. It is guaranteed that no road is given twice.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ roads.length ≤ 5000</code>,<br />
<code>roads[i].length = 2</code>,<br />
<code>0 ≤ roads[i][j] &lt; cities</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>A unique array of roads that should be built sorted as described above. There's no need to build looping roads, i.e. roads that lead back from a city to itself.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
