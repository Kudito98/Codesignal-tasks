<p>You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and you have taught it to recognized several patterns.</p>
<p>You are pretty pleased with your results so far and as such you have finally decided to put your program to good use. The timing is perfect: you've received an offer from a jewelery shop. They want you to help them sort their diamonds. Each gem has a different type of a cut which influences its price. You were asked to find all the diamonds with the specific kind of pattern.</p>
<p>Luckily, your image recognizer has almost everything it takes to tackle the problem,and all that is left for you it is to teach it to recognize <em>correct</em> patterns. You need to implement a function that, given the <a href="keyword://adjacency-matrix-unweighted" target="_blank">adjacency matrix</a> representing the cut contour, will determine whether it's a <em>correct</em> or not.</p>
<p>The pattern of the cut of size <code>2 · n</code> is a <em>correct</em> one if its contour can be split into two equal groups <code>U</code> and <code>V</code> of <code>n</code> vertices numbered from <code>0</code> to <code>n - 1</code> (in each group) such that for any pair of vertices <code>u</code> and <code>v</code> there exists an edge between them if and only if they don't belong to the same group and their respective "group" numbers are different.</p>
<p>Here are some examples of <em>correct</em> cut contours (vertices belonging to the same group have the same color).</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isCorrectlyCut/img/diamonds.png?_tm=1624357929604" alt="Diamonds" /></p>
<p>Given the gem's contour as an undirected graph represented by its adjacency matrix <code>adj</code> determine whether it has a <em>correct</em> cut or not.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>adj = [[false, true, false, false, false, true],
       [true, false, true, false, false, false],
       [false, true, false, true, false, false],
       [false, false, true, false, true, false],
       [false, false, false, true, false, true],
       [true, false, false, false, true, false]]
</code></pre>
<p>the output should be<br />
<code>solution(adj) = true</code>.</p>
<p>Here's how the given graph looks like (here <code>gn</code> stands for the vertex number in its group):</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isCorrectlyCut/img/example1.png?_tm=1624357929865" alt="Example" /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.boolean adj</strong></p>
<p>An adjacency matrix of an undirected graph with <em>even</em> number of vertices.</p>
<p><em>Guaranteed constraints:</em><br />
<code>6 ≤ adj.length ≤ 100</code>,<br />
<code>adj[i].length == adj.length</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the given contour is a contour of the correct diamond cut, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
