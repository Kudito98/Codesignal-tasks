<p>Once upon a time, in a kingdom far, far away, there lived a King Byteasar III. As a smart and educated ruler, he did everything in his (unlimited) power to make every single system within his kingdom efficient. The king went down in history as a great road builder: during his reign a great number of roads were built, and the road system he created was the most efficient during those dark times.</p>
<p>When you started learning about Byteasar's III deeds in your history classes, a creeping doubt crawled into the back of your mind: what if the famous king wasn't so great after all? According to the most recent studies, there were <code>n</code> cities in Byteasar's kingdom, connected by two-way <code>roads</code>. You managed to get information about these <code>roads</code> from the university library, so now you can write a function that will determine whether the road system in Byteasar's kingdom was efficient or not.</p>
<p>A road system is considered efficient if it is possible to travel from any city to any other city by traversing at most <code>2</code> roads.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 6</code> and</p>
<pre><code>roads = [[3, 0], [0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
</code></pre>
<p>the output should be<br />
<code>solution(n, roads) = true</code>.</p>
<p>Here's how the road system can be represented:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/efficientRoadNetwork/img/example1.jpg?_tm=1624350030711" alt /></p>
</li>
<li>
<p>For <code>n = 6</code> and</p>
<pre><code>roads = [[0, 4], [5, 0], [2, 1],
          [1, 4], [2, 3], [5, 2]]
</code></pre>
<p>the output should be<br />
<code>solution(n, roads) = false</code>.</p>
<p>Here's how the road system can be represented:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/efficientRoadNetwork/img/example2.jpg?_tm=1624350031027" alt /></p>
<p>As you can see, it's only possible to travel from city <code>3</code> to city <code>4</code> by traversing at least <code>3</code> roads.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 7 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of cities in the kingdom.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 250</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer roads</strong></p>
<p>Array of roads in the kingdom. Each road is given as a pair <code>[<i>city<sub>i</sub></i>, <i>city<sub>j</sub></i>]</code>, where <code>0 ≤ <i>city<sub>i</sub></i>, <i>city<sub>j</sub></i> &lt; n</code> and <code><i>city<sub>i</sub></i> ≠ <i>city<sub>j</sub></i></code>. It is guaranteed that no road is given twice.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ roads.length ≤ 35000</code>,<br />
<code>roads[i].length = 2</code>,<br />
<code>0 ≤ roads[i][j] &lt; n</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the road system is efficient, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
