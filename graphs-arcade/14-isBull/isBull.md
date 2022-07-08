<p>You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.</p>
<p>Today you want to teach your program to recognize <em>bull</em> patterns, which means that you need to implement a function that, given the <a href="keyword://adjacency-matrix-unweighted" target="_blank">adjacency matrix</a> representing the contour, will determine whether it's a <em>bull</em> or not.</p>
<p>You noticed that although all <em>bull</em> heads are similar there is some variation in the shapes of their horns, so there are several possible bull contours. The image below shows <em>all</em> such contours.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isBull/img/bulls.png?_tm=1624357927747" alt="Bulls" /></p>
<p>Given the object's contour as an undirected graph represented by adjacency matrix <code>adj</code> determine whether it's a <em>bull</em> or not.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>adj = [[false, true, false, false, false],
       [true, false, true, true, false],
       [false, true, false, true, false],
       [false, true, true, false, true],
       [false, false, false, true, false]]
</code></pre>
<p>the output should be<br />
<code>solution(adj) = true</code>.</p>
<p>Here's how the given graph looks like:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isBull/img/example1.png?_tm=1624357928010" alt="Example" /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean adj</strong></p>
<p>An adjacency matrix of an undirected graph.</p>
<p><em>Guaranteed constraints:</em><br />
<code>adj.length == 5</code>,<br />
<code>adj[i].length == 5</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the given contour is a bull, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
