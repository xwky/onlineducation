<template>
	<div>
		<div class="freeback-container">
			<div class="freeback-img-box">
				<img src="static/image/freeback.png">
			</div>
			<div class="freeback-box-border">
				<div class="freeback-box">
					<div class="freeback-title">
						<h1>意见反馈</h1>
						<h2>感谢你的反馈，我们会积极改善，做出更好的服务的</h2>
					</div>
					<div class="freeback-content">
						<div class="freeback-form">
							<Form :model="formItem" :label-width="80" :rules="ruleInline">
								<FormItem label="标题" prop="title">
									<i-input v-model="formItem.title" placeholder="请输入标题"></i-input>
								</FormItem>
								<FormItem label="反馈信息" prop="info">
									<i-input v-model="formItem.info" type="textarea" :autosize="{minRows: 8,maxRows: 10}" placeholder="请输入反馈信息"></i-input>
								</FormItem>
								<FormItem>
									<Button type="primary" @click='submmit();two()'>提交</Button>
									<Button  @click='clear'>清空信息</Button>
								</FormItem>
							</Form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Freeback',
		data() {
			return {
				formItem: {
					title: '',
					info: ''
				},
				ruleInline: {
					title: [{
						required: true,
						message: '请输入标题',
						trigger: 'blur'
					}],
					info: [{
						required: true,
						message: '请输入反馈信息',
						trigger: 'blur'
					}]
				}
			};
		},
		created() {
			this.submmit(),
				this.clear()


		},
		methods: {
      change(){
            window.location.reload();        
        },

			submmit: function() {
				const params = {
					title: this.formItem.title,
					info: this.formItem.info,
				};
				this.axios.post('http://127.0.0.1:8000/api/course/freeback/', {
					...params
				})
			},
			two: function() {
				if (this.formItem.title == '' || this.formItem.info == '') {
					this.$Message.error('反馈失败');
				} else {
					this.$router.push({
						path: '/freeback',
						query: {
							formItem: 'fankui'
						}
          });
          this.formItem.title = ''
				  this.formItem.info = ''
          this.$Message.success('反馈成功');
				}
			},


			clear() {
				this.formItem.title = ''
				this.formItem.info = ''
			}

		}

	};
</script>

<style scoped>
	.freeback-container {
		margin: 15px auto;
		width: 80%;
		height: 600px;
		display: flex;
		align-items: center;
		/* background-color: #ccc; */
	}

	.freeback-img-box {
		width: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.freeback-img-box img {
		width: 80%;
	}

	.freeback-box-border {
		width: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.freeback-box {
		width: 480px;
	}

	.freeback-content {
		margin: 15px auto;
		border: 1px #ccc dotted;
	}

	.freeback-form {
		margin: 30px auto;
		width: 90%;
	}
</style>
