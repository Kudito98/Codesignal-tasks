<p>Once upon a time, in a kingdom far, far away, there lived a King Byteasar VII. Since he reigned during the Dark Times, very little is known about his reign. It is known that when he ascended the throne, there were <code>n</code> cities in the kingdom, connected by several two-way <code>roads</code>. But before the young king managed to start ruling, an enemy arrived at the gates: the evil emperor Bugoleon invaded the kingdom and started to conquer the cities, advancing day after day.</p>
<p>It is not known how long it took to capture each of the cities, but you've recently discovered an ancient manuscript describing that each day, Bugoleon captured all the cities that had at most <code>1</code> neighboring free city at that given moment. Knowing this fact, the number of cities <code>n</code> and all the <code>roads</code> of the kingdom, determine in how many days each of the cities was conquered.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>n = 10</code> and</p>
<pre><code>roads = [[1, 0], [1, 2], [8, 5], [9, 7], 
         [5, 6], [5, 4], [4, 6], [6, 7]]
</code></pre>
<p>the output should be<br />
<code>solution(n, roads) = [1, 2, 1, 1, -1, -1, -1, 2, 1, 1]</code>.</p>
<p>Here's how the cities were conquered:<br />
<img src="https://codesignal.s3.amazonaws.com/tasks/citiesConquering/img/example.jpg?_tm=1624348811651" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of cities in the kingdom.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer roads</strong></p>
<p>Array of two-way roads, where each road is given in the format <code>[<em>city<sub>1</sub></em>, <em>city<sub>2</sub></em>]</code>, meaning that <code><em>city<sub>1</sub></em></code> and <code><em>city<sub>2</sub></em></code> are connected. It is guaranteed that there is at most one road between two cities, and no road is given twice.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ roads.length ≤ n · (n - 1) / 2</code>,<br />
<code>roads[i].length = 2</code>,<br />
<code>roads[i][0] ≠ roads[i][1]</code>,<br />
<code>0 ≤ roads[i][j] &lt; n</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>An array of length <code>n</code>, there the <code>i<sup>th</sup></code> element is the number of days it took to conquer the <code>i<sup>th</sup></code> city, or <code>-1</code> if the city wasn't conquered.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
