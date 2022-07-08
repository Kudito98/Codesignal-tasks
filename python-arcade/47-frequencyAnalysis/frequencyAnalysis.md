<p>You've recently read "The Gold-Bug" by Edgar Allan Poe, and was so impressed by the cryptogram in it that decided to try and decipher an encrypted text yourself. You asked your friend to encode a piece of text using a substitution cipher, and now have an <code>encryptedText</code> that you'd like to decipher.</p>
<p>The encryption process in the story you read involves <em>frequency analysis</em>: it is known that letter <code>'e'</code> is the most frequent one in the English language, so it's pretty safe to assume that the most common character in the <code>encryptedText</code> stands for <code>'e'</code>. To begin with, implement a function that will find the most frequent character in the given <code>encryptedText</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>encryptedText = "$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ"</code>,<br />
the output should be<br />
<code>solution(encryptedText) = 'C'</code>.</p>
<p>Letter <code>'C'</code> appears in the text more than any other character (<code>4</code> times), which is why it is the answer.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string encryptedText</strong></p>
<p>Encrypted text consisting of various ASCII characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ encryptedText.length ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] char</strong></p>
<p>The most common character in the <code>encryptedText</code>. The output is guaranteed to be unique.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
