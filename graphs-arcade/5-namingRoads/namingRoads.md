<p>Once upon a time, in a kingdom far, far away, there lived a King Byteasar V. His predecessor, King Byteasar IV, lived quite a long life, and when Byteasar V finally ascended to the throne, he was already 150 years old. The new king had been preparing all his life for his moment of glory and, scared that he wouldn't have enough time to shine, started his reforms right away. The first (and, as it turned out, the last) royal decree, issued within a couple of days of the coronation, ordered the following: each and every <code>road</code> in the kingdom was to be named.</p>
<p>Unfortunately the king didn't have enough time to come up with actual names, so all the <code>roads</code> were to be names with numbers from <code>0</code> to <code>roads.length - 1</code>. As a born strategist, Byteasar wanted to make sure that the maps of his kingdom were confusing to enemies, which is why the road names were to be chosen so that no two roads with neighboring names would have a common end.</p>
<p>The official cartographers came up with names for the <code>roads</code>, but they're not sure if the constraint the king imposed was actually met, and it's your job to help them out. Given the names for the <code>roads</code> the cartographers came up with, check that no two roads with neighboring names have a common end.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For</p>
<pre><code>roads = [[0, 1, 0],
         [4, 1, 2],
         [4, 3, 4],
         [2, 3, 1],
         [2, 0, 3]]
</code></pre>
<p>the output should be<br />
<code>solution(roads) = true</code>.</p>
<p>Here's what the given road system looks like:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/namingRoads/img/example1.jpg?_tm=1624355815915" alt /></p>
</li>
<li>
<p>For</p>
<pre><code>roads = [[2, 3, 1],
         [3, 0, 0],
         [2, 0, 2]]
</code></pre>
<p>the output should be<br />
<code>solution(roads) = false</code>.</p>
<p>Here's what the given road system looks like:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/namingRoads/img/example2.jpg?_tm=1624355816129" alt /></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer roads</strong></p>
<p>Array of two-way roads with their names. Each road is given in the format <code>[<em>city<sub>1</sub></em>, <em>city<sub>2</sub></em>, <em>road_name</em>]</code>, where <code><em>city<sub>1</sub></em> ≠ city<sub>2</sub></code>, and <code>0 ≤ <em>road_name</em> &lt; roads.length</code>. It is guaranteed that there are no duplicate roads or roads with the same name.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ roads.length ≤ 35000</code>,<br />
<code>roads[i].length = 3</code>,<br />
<code>roads[i][0] ≠ roads[i][1]</code>,<br />
<code>0 ≤ roads[i][2] &lt; roads.length</code>,<br />
<code>0 ≤ roads[i][j] ≤ 35000</code>,<br />
<code>roads[i][2] ≠ roads[j][2], i ≠ j</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the names of the roads will be confusing to enemies, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
