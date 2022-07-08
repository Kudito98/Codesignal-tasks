<p>You are standing at a magical well. It has two positive integers written on it: <code>a</code> and <code>b</code>. Each time you cast a magic marble into the well, it gives you <code>a * b</code> dollars and then both <code>a</code> and <code>b</code> increase by 1. You have <code>n</code> magic marbles. How much money will you make?</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = 1</code>, <code>b = 2</code>, and <code>n = 2</code>, the output should be<br />
<code>solution(a, b, n) = 8</code>.</p>
<p>You will cast your first marble and get <code>$2</code>, after which the numbers will become <code>2</code> and <code>3</code>. When you cast your second marble, the well will give you <code>$6</code>. Overall, you'll make <code>$8</code>. So, the output is <code>8</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer a</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a ≤ 2000</code>.</p>
</li>
<li>
<p><strong>[input] integer b</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ b ≤ 2000</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of magic marbles in your possession, a non-negative integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ n ≤ 5</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
