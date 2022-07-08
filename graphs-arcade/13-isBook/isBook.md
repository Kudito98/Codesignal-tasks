<p>You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.</p>
<p>Today you want to teach your program to recognize <em>book</em> patterns, which means that you need to implement a function that, given the <a href="keyword://adjacency-matrix-unweighted" target="_blank">adjacency matrix</a> representing the contour, will determine whether it's a <em>book</em> or not.</p>
<p>A <em>book</em> consists of a base and may have any number of pages.<br />
The <em>book</em>'s base consists of a single edge connecting two nodes, and it is a common edge for all the pages. Besides that, every page has only one node connected to both sides of the base.<br />
Here is an example of a <em>book</em>:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isBook/img/book.png?_tm=1624350035264" alt="Book" /></p>
<p>Given the object's contour as an undirected graph represented by its <a href="keyword://adjacency-matrix-unweighted" target="_blank">adjacency matrix</a> <code>adj</code> determine whether it's a <em>book</em> or not.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>adj = [[false, true, true, true],
       [true, false, true, true],
       [true, true, false, false],
       [true, true, false, false]]
</code></pre>
<p>the output should be<br />
<code>solution(adj) = true</code>.</p>
<p>Here's how the given graph looks like:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isBook/img/example1.png?_tm=1624350035494" alt="Example" /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean adj</strong></p>
<p>An adjacency matrix of an undirected graph.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ adj.length &lt; 100</code>,<br />
<code>adj[i].length == adj.length</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the given contour is a <em>book</em>, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
