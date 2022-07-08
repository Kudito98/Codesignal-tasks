<p>You and your friend are walking in the woods. You are gathering mushrooms and catching butterflies, and your friend is drawing a map of the woods: he is a very cautious person, who doesn't want to get lost. When you get tired of running around, you decide to check out the map your friend has drawn so far, and it strikes you: looks like the woods you're walking in represent a <em>pseudoforest</em>!</p>
<p>Since you're a programmer and think in terms of algorithms, you need to write a function that, given a map, determines whether it is a <em>pseudoforest</em> or not. The map your friend drew represents a graph <code>wmap</code> of <code>n</code> vertices. A map is called <em>pseudoforest</em> if each of its <a href="keyword://connected-component" target="_blank">connected components</a> contains no more than one cycle.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 7</code> and <code>wmap = [[0, 1], [1, 2], [2, 3], [3, 1], [3, 4], [5, 6]]</code>, the output should be<br />
<code>solution(n, wmap) = true</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isPseudoforest/img/example1.png?_tm=1624357937406" alt /></p>
<p>One of the connected components contains only one cycle (<code>1 - 2 - 3</code>), and the other one has no cycles at all.</p>
</li>
<li>
<p>For <code>n = 7</code> and <code>wmap = [[0, 1], [1, 2], [2, 3], [3, 1], [3, 4], [4, 0], [5, 6]]</code>, the output should be<br />
<code>solution(n, wmap) = false</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isPseudoforest/img/example2.png?_tm=1624357937617" alt /></p>
<p>There are three cycles in one of the connected components:</p>
<ul>
<li><code>1 - 2 - 3</code>;</li>
<li><code>1 - 3 - 4 - 0</code>;</li>
<li><code>0 - 1 - 2 - 3 - 4</code>.</li>
</ul>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>Number of vertices in a map.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer wmap</strong></p>
<p>Edges drawn on the map. <code>wmap[i]</code> contains two elements and represents one edge for each valid <code>i</code>.<br />
It is guaranteed that between any two vertices there is no more than one edge.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ wmap.length ≤ 10<sup>5</sup></code>,<br />
<code>wmap[i].length = 2</code>,<br />
<code>0 ≤ wmap[i][j] &lt; n</code>,<br />
<code>wmap[i][0] ≠ wmap[i][1]</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>wmap</code> represents a <em>pseudoforest</em> and <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
