<!DOCTYPE html>
<html lang="en">
<head>

	<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>SB Admin 2 - Bootstrap Admin Theme</title>

	<?php include('../common/head.php') ?>
<!-- Page Content -->
			
<div id="page-wrapper">
	<div class="container-fluid">
		 <div class="row">
			<div class="col-lg-12">
			
				<h3 class="page-header">Internation Journal of Chemistry</h3>
				
				<div class="panel panel-info" >
					
					<div class="panel-body">
                            <!-- Nav tabs -->
                            <ul class="nav nav-tabs">
                                <li class="active"><a href="#home" data-toggle="tab">Home</a>
                                </li>
                                <li><a href="#eb" data-toggle="tab">Editorial Board</a>
                                </li>
                                <li><a href="#rb" data-toggle="tab">Reviewer Board</a>
                                </li>
                                <li><a href="#archives" data-toggle="tab">Archives</a>
                                </li>
								<li><a href="#spis" data-toggle="tab">Special Issues</a>
                                </li>
								<li><a href="#sm" data-toggle="tab">Submit Manuscript</a>
                                </li>
                            </ul>

                            <!-- Tab panes -->
                            <div class="tab-content">
                                <div class="tab-pane fade in active" id="home">
                                    <?php include('homepage.php');?>
								</div>
                                
								<div class="tab-pane fade" id="eb">
                                    <?php include('eb.php');?>
                                </div>
                                
								<div class="tab-pane fade" id="rb">
                                    <?php include('rb.php');?>
                                </div>
                                
								<div class="tab-pane fade" id="archives">
                                    <?php include('archives.php');?>
                                </div>
                                
								<div class="tab-pane fade" id="spis">
                                    <?php include('special_issues.php');?>
                                </div>
                                
								<div class="tab-pane fade" id="sm">
                                    <?php include('submissionForm.php');?>
                                </div>
								
                            </div>
                        </div>
					
					
					
					
				</div>
				
			</div>	<!-- /.col-lg-12 -->
		</div>
	</div><!-- /.container-fluid -->  
</div><!-- /#page-wrapper -->
<?php include('../common/foot.php') ?>
