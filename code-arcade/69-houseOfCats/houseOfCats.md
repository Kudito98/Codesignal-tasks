<p>There are some people and cats in a house. You are given the number of legs they have all together. Your task is to return an array containing every possible number of people that could be in the house <em>sorted in ascending order</em>. It's guaranteed that each person has <code>2</code> legs and each cat has <code>4</code> legs.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>legs = 6</code>, the output should be<br />
<code>solution(legs) = [1, 3]</code>.</p>
<p>There could be either <code>1</code> cat and <code>1</code> person (<code>4 + 2 = 6</code>) or <code>3</code> people (<code>2 * 3 = 6</code>).</p>
</li>
<li>
<p>For <code>legs = 2</code>, the output should be<br />
<code>solution(legs) = [1]</code>.</p>
<p>There can be only <code>1</code> person.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer legs</strong></p>
<p>The total number of legs in the house. It's guaranteed,that this number is even.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ legs &lt; 50</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>Every possible number of people that can be in the house.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
