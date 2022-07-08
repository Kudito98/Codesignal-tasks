<p>Wandering in the woods, you noticed a squirrel sitting in node <code>A</code> of a <a href="keyword://tree" target="_blank">tree</a>. It didn't look like it was going to sit there forever though: there was a delicious nut in node <code>B</code>, and the squirrel looked determined to reach it by moving via the branches of the <em>tree</em>. You grabbed your camera to take a picture of the squirrel in node <code>C</code> (that's the only node that would make the picture perfect), but was too late: the smart rodent had already made it to node <code>B</code>.</p>
<p>There are still a lot of nuts on the <em>tree</em>, and it seems that the squirrel is going to try and take them all. Looks like the squirrel is smart enough to follow only the shortest paths along the <em>tree</em> branches, which means you can now predict when the right opportunity to take a perfect picture arises. Given configuration of the <code>tree</code> and a bunch of <code>triples</code> consisting of numbers <code>A</code>, <code>B</code> and <code>C</code>, for each triple return <code>true</code> if the squirrel will run through node <code>C</code> on its path from <code>A</code> to <code>B</code>, and <code>false</code> otherwise.</p>
<p><strong>It is guaranteed that each node has no more than <code>5</code> branches</strong>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>tree = [1, 2,
        1, 3,
        2, 4,
        3, 5,
        3, 6]
</code></pre>
<p>and</p>
<pre><code>triples = [[4, 6, 3],
           [1, 4, 2],
           [5, 6, 1]]
</code></pre>
<p>the output should be<br />
<code>solution(tree, triples) = [true, true, false]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer tree</strong></p>
<p>An array of integers of even length, where a pair <code>(tree[i], tree[i + 1])</code> for every even <code>i</code> corresponds to the branch in a <code>tree</code> that goes from node <code>tree[i]</code> to <code>tree[i + 1]</code>, both 1-based.</p>
<p><em>Guaranteed constraints:</em><br />
<code>tree.length = 2 · (max(tree) - 1)</code>,<br />
<code>1 ≤ tree[i] ≤ 10000</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer triples</strong></p>
<p>Triples of three integers in the format <code>[A, B, C]</code>, where <code>A</code> stands for the initial squirrel position, <code>B</code> stands for its destination and <code>C</code> stands for the node at which the perfect picture can be taken, all 1-based.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ triples.length ≤ 10000</code>,<br />
<code>triples[i].length = 3</code>,<br />
<code>1 ≤ triples[i][j] ≤ n</code>.</p>
</li>
<li>
<p><strong>[output] array.boolean</strong></p>
<p>Array of the same length as <code>triples</code>, where the <code>i<sup>th</sup></code> element is <code>true</code> if and only if it will be possible to take a perfect picture in the situation corresponding to the <code>i<sup>th</sup></code> triple.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
