<p>You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.</p>
<p>Today you want to teach your program to recognize <em>wheel</em> patterns, which means that you need to implement a function that, given the <a href="keyword://adjacency-matrix-unweighted" target="_blank">adjacency matrix</a> representing the contour, will determine whether it's a <em>wheel</em> or not.</p>
<p>The <em>wheel</em> contour can be thought of as a single center vertex and a regular polygon with <code>n</code> (<code>n &gt; 2</code>) vertices which are all connected to the center. Here is an example:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isWheel/img/wheel.png?_tm=1624355812643" alt="A wheel" /></p>
<p>Given the object's contour as an undirected graph represented by its <em>adjacency matrix</em> <code>adj</code> determine whether it's a <em>wheel</em> or not.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>adj = [[false, true, true, true, true],
       [true, false, true, false, true],
       [true, true, false, true, false],
       [true, false, true, false, true],
       [true, true, false, true, false]]
</code></pre>
<p>the output should be<br />
<code>solution(adj) = true</code>.</p>
<p>Here's what the given graph looks like:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isWheel/img/example1.png?_tm=1624355812850" alt="Example" /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean adj</strong></p>
<p>An adjacency matrix of an undirected graph.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 &lt; adj.length &lt; 100</code>,<br />
<code>adj[i].length == adj.length</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the given contour is a <em>wheel</em>, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
