<p>You've been working on a particularly difficult algorithm all day, and finally decided to take a break and drink some coffee. To your horror, when you returned you found out that your cat decided to take a walk on the keyboard in your absence, and pressed a key or two. Your computer doesn't react to letters being pressed when an unauthorized action appears, but allows typing whitespace characters and moving the arrow keys, so now your masterpiece contains way too many whitespace characters.</p>
<p>To repair the damage, you need to start with implementing a function that will replace all multiple space characters in the given <code>line</code> of your code with single ones. In addition, all leading and trailing whitespaces should be removed.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>line = "def      m   e  gaDifficu     ltFun        ction(x):"
</code></pre>
<p>the output should be<br />
<code>solution(line) = "def m e gaDifficu ltFun ction(x):"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string line</strong></p>
<p>One line from your code containing way too many whitespace characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ line.length ≤ 125</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p><code>line</code> with unnecessary whitespace characters removed.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
