<p>Not long ago you discovered a wonderful tree in the nearby woods that made you very curious about the greenery around you. You went to the nearby woods and drew various plants in your notebook. The plants in the woods have various structures: some of them even contain loops!</p>
<p>Anyway, for now you are interested only in <a href="keyword://tree" target="_blank">trees</a>. You came up with a brand new property: you call a tree a <em>caterpillar</em> if there exists a path in it, such that each vertex of a tree either belongs to this path or is connected to one of its vertices by a single edge. To find out more about them, you would like to write a program that will find all interesting <em>trees</em> in the structures you drew in your notebook.</p>
<p>The plants you drew consist of <code>n</code> vertices and are connected by several <code>edges</code>. Calculate the number of regular <em>trees</em> and <em>caterpillar trees</em> in the structures you drew in your notebook.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 21</code> and</p>
<pre><code>edges = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [4, 7],
         [4, 8], [4, 9], [4, 10], [10, 11], [11, 12], [11, 13],
         [11, 14], [14, 15], [14, 16], [14, 17], [14, 18], [14, 19]]
</code></pre>
<p>the output should be <code>solution(n, edges) = [2, 2]</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/caterpillarTrees/img/example1.png?_tm=1624350021227" alt /></p>
<p>There are two connected components and both of them are <em>trees</em> and <em>caterpillar</em> trees.</p>
</li>
<li>
<p>For <code>n = 22</code> and</p>
<pre><code>edges = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [4, 7],
         [4, 8], [4, 9], [4, 10], [10, 11], [11, 12], [11, 13],
         [11, 14], [14, 15], [14, 16], [14, 17], [14, 18], [14, 19], [13, 20]]
</code></pre>
<p>the output should be <code>solution(n, edges) = [2, 1]</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/caterpillarTrees/img/example2.png?_tm=1624350021459" alt /></p>
<p>The first connected component is a <em>tree</em>, but not a <em>caterpillar</em> tree, because vertex <code>20</code> is not directly connected to the central path.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of vertices in the structures drawn in your notebook.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer edges</strong></p>
<p>Edges drawn in the notebook. <code>edges[i]</code> for each valid <code>i</code> contains two elements and represents an edge that connects <code>edges[i][0]</code> and <code>edges[i][1]</code>.<br />
It is guaranteed that between any two vertices there is no more than one edge.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ edges.length ≤ 10<sup>5</sup></code>,<br />
<code>edges[i].length = 2</code>,<br />
<code>0 ≤ edges[i][j] &lt; n</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Array of two integers, where the first represents the number of <em>trees</em> in your woods and the second represents the number of <em>caterpillar</em> trees in it.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
