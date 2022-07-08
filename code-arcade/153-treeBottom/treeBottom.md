<p>You are given a recursive notation of a binary tree: each node of a tree is represented as a set of three elements:</p>
<ul>
<li>value of the node;</li>
<li>left subtree;</li>
<li>right subtree.</li>
</ul>
<p>So, a tree can be written as <code>(value left_subtree right_subtree)</code>. It is guaranteed that <code>1 ≤ value ≤ 10<sup>9</sup></code>. If a node doesn't exist then it is represented as an empty set: <code>()</code>. For example, here is a representation of a tree in the given picture:</p>
<pre><code>(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))
</code></pre>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/treeBottom/img/tree.png?_tm=1624437065862" alt /></p>
<p>Your task is to obtain a list of nodes, that are the most distant from the tree root, in the order from left to right.</p>
<p>In the notation of a node its value and subtrees are separated by exactly one space character.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>tree = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"
</code></pre>
<p>the output should be<br />
<code>solution(tree) = [5, 11, 4]</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string tree</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>9 ≤ tree.length ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>The values of the nodes that are the most distant from the tree root.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
