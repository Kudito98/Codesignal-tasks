<p>Given a string consisting of lowercase English letters, find the largest square number which can be obtained by <em>reordering</em> the string's characters and <em>replacing</em> them with any digits you need (leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.</p>
<p>If there is no solution, return <code>-1</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>s = "ab"</code>, the output should be<br />
<code>solution(s) = 81</code>.<br />
The largest <code>2</code>-digit square number with different digits is <code>81</code>.</li>
<li>For <code>s = "zzz"</code>, the output should be<br />
<code>solution(s) = -1</code>.<br />
There are no <code>3</code>-digit square numbers with identical digits.</li>
<li>For <code>s = "aba"</code>, the output should be<br />
<code>solution(s) = 900</code>.<br />
It can be obtained after reordering the initial string into <code>"baa"</code> and replacing "a" with <code>0</code> and "b" with <code>9</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string s</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ s.length &lt; 10</code>.</p>
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
