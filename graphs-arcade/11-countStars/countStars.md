<p>You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.</p>
<p>Today you want to teach your program to recognize <em>star</em> patterns in the image of the night sky, which means that you need to implement a function that, given the <a href="keyword://adjacency-matrix-unweighted" target="_blank">adjacency matrix</a> representing a number of contours in the sky, will find the number of <em>stars</em> in it.</p>
<p>The graph representing some contour is cosidered to be a <em>star</em> if it is a <a href="keyword://tree" target="_blank">tree</a> of size <code>2</code> or if it is a tree of size <code>k &gt; 2</code> with one internal node (which is a tree root at the same time) and <code>k - 1</code> leaves.<br />
Here is an example of some stars:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/countStars/img/stars.png?_tm=1624350027450" alt="Stars" /></p>
<p>Given the sky objects' contours as an undirected graph represented by its adjacency matrix <code>adj</code>, calculate the number of <em>stars</em> in it.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>adj = [[false, true, false, false, false],
       [true, false, false, false, false],
       [false, false, false, true, false],
       [false, false, true, false, false],
       [false, false, false, false, false]]
</code></pre>
<p>the output should be<br />
<code>solution(adj) = 2</code>.</p>
<p>Here's what the given graph looks like:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/countStars/img/example1.png?_tm=1624350027688" alt="Example" /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean adj</strong></p>
<p>An adjacency matrix of an undirected graph.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 &lt; adj.length ≤ 100</code>,<br />
<code>adj[i].length == adj.length</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of <em>star</em> contours in the sky.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
