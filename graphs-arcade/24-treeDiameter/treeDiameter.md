<p>You got sick because of walking in the woods at night, and have to spend a week at home without going out. Looking out of the window at the nearby woods you're wondering if there is anything you don't yet know about them. Suddenly you see a beautiful and very tall <a href="keyword://tree" target="_blank">tree</a> you haven't seen before. Since you have nothing to do, you decide to examine its structure and draw it in your notebook.</p>
<p>You became so exited about this new tree that your temperature went up, so you were forced to stay in bed. You can't see the tree from your bed, but luckily you have it drawn down. The first thing you'd like to find out about is the tree height. Looking at your drawing you suddenly realize that you forgot to mark the tree bottom and you don't know from which vertex you should start counting. Of course a tree height can be calculated as the length of the longest path in it (it is also called <a href="keyword://diameter" target="_blank">tree diameter</a>). So, now you have a task you need to solve, so go ahead!</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>n = 10</code> and</p>
<pre><code>tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]
</code></pre>
<p>the output should be <code>solution(n, tree) = 7</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/treeDiameter/img/example1.png?_tm=1624362029910" alt /></p>
<p>The longest path is the path from vertex <code>4</code> to one vertex <code>9</code> or <code>0</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of vertices in the structure you drew in your notebook.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer tree</strong></p>
<p>Edges of the tree. <code>tree[i]</code> for each valid <code>i</code> contains two elements and represents an edge that connects <code>tree[i][0]</code> and <code>tree[i][1]</code>.<br />
It is guaranteed that given graph is a tree, i.e. it is connected and has no cycles.</p>
<p><em>Guaranteed constraints:</em><br />
<code>tree.length = n - 1</code>,<br />
<code>tree[i].length = 2</code>,<br />
<code>0 ≤ tree[i][j] &lt; n</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p><em>tree diameter</em> of the given tree.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
